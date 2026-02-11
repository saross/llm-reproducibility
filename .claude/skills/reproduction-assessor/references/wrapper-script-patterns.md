# Wrapper Script Patterns for Batch Execution

Reference document for converting interactive R scripts into batch-executable
scripts suitable for Docker containers and automated reproduction pipelines.

## When Wrapper Scripts Are Needed

Interactive R scripts designed for RStudio cannot be run in Docker containers
without modification. Common indicators that a wrapper is required:

- Scripts use `View()`, interactive `print()`, or manual variable inspection
- Parameters are changed by commenting/uncommenting lines rather than
  programmatically
- The script must be run multiple times with different settings
- No output saving — plots go to the RStudio viewer, not to files
- Incremental code blocks in supplementary materials, designed for copy-paste
  execution rather than end-to-end batch runs

## The Cardinal Rule

**NO algorithmic modifications.** Wrapper scripts reorganise execution flow and
add output capture, but must never change:

- Statistical methods or parameters
- Data filtering or subsetting logic
- Model specifications
- The order of analytical steps (unless genuinely independent)
- Variable names used in calculations

The wrapper is infrastructure, not analysis. If a reviewer cannot distinguish
the analytical results of the wrapper from the original script, the wrapper is
correct. If results differ, the wrapper has introduced a bug.

## Parameterised Function Pattern

For scripts that must be run multiple times with different parameters (e.g.,
Herskind n-gram sizes 2, 3, 4), wrap the core logic in a function and iterate:

```r
# Original: manually change n <- 2 to n <- 3, n <- 4
# Wrapper: parameterise

run_analysis <- function(n, output_prefix) {
  # ... original analysis code unchanged ...
  write.csv(results, paste0("outputs/", output_prefix, "_results.csv"))
}

for (n in c(2, 3, 4)) {
  run_analysis(n, paste0(n, "gram"))
}
```

This pattern preserves all analytical logic while eliminating manual
intervention between runs. The function boundary also makes variable scoping
explicit, preventing accidental state leakage between iterations.

## Output Capture Patterns

Interactive scripts typically rely on the RStudio viewer and console for output.
In batch mode, all outputs must be written to files explicitly.

### Plots

Wrap plot generation in a graphics device:

```r
# Using pdf/png device
pdf("outputs/figure-1.pdf", width = 8, height = 6)
plot(x, y)
dev.off()

# Using ggsave for ggplot objects
p <- ggplot(data, aes(x, y)) + geom_point()
ggsave("outputs/figure-2.png", p, width = 8, height = 6, dpi = 300)
```

### Tables

```r
write.csv(results_table, "outputs/results-table.csv", row.names = FALSE)
```

### Console Output

```r
# Capture all console output for a block
sink("outputs/run.log")
# ... analysis code ...
sink()
```

### Statistical Summaries

```r
# Original: print(summary(model))
# Wrapper: capture to file
sink("outputs/summary-stats.txt")
print(summary(model))
sink()

# Alternative using capture.output
capture.output(summary(model), file = "outputs/model-summary.txt")
```

## Incremental Code Block Assembly

Supplementary materials often present code in numbered sections (e.g., Dye
sections 5.1–5.38) intended for sequential copy-paste execution. Converting
these to a single executable script requires care:

- **Read all sections sequentially** — understand the cumulative state before
  writing the wrapper
- **Track variable state** — note list indices, accumulated objects, and any
  variables that carry forward between sections
- **Verify column names against actual data** — PDF line-wrapping can break
  strings, introducing spurious whitespace or splitting variable names across
  lines
- **Use named list construction** (`$` access) instead of positional indexing
  for robustness — positional indices are fragile if earlier sections change
- **Test incrementally** — run the first few sections, verify outputs match
  expectations, then add more sections progressively

This is the most error-prone pattern because the original authors tested each
block interactively, inspecting intermediate results. The wrapper must produce
the same intermediate state without that inspection.

## Literate Programming Pattern

For Rmd (R Markdown) or Qmd (Quarto) files, rendering is the execution
mechanism:

```r
# In Dockerfile or wrapper script:
rmarkdown::render("analysis.Rmd", output_dir = "outputs/")

# Or for Quarto (called from shell, not R):
# quarto render analysis.qmd
```

Two architectural approaches exist for Docker integration:

- **Build-as-render**: The Dockerfile renders the document during
  `docker build`, baking outputs into the image. Reproducibility is captured at
  build time.
- **Runtime render**: The container renders via `CMD` or an entrypoint wrapper
  script. Outputs are generated at `docker run` and can be extracted via volume
  mounts.

The runtime approach is generally preferable for reproduction work, as it
separates environment construction from analysis execution and makes output
extraction straightforward.

## Parameterised Loop Pattern (Multi-Dataset)

For papers that apply the same analysis to multiple datasets and/or variables (e.g.,
Key et al. 2024: 5 Olduvai variables, then 4 Paleoindian types × 4 variables), use
nested loops with a load → subset → analyse → extract pattern:

```r
# Load all datasets once
olduvai <- read.csv("data/olduvai-cleavers.csv")
paleoindian <- read.csv("data/paleoindian-points.csv")

# Define analysis parameters
olduvai_vars <- c("length_mm", "breadth_mm", "thickness_mm", "edge_length_mm", "mass_g")
paleo_types <- c("Clovis", "E.Clovis", "Folsom", "Midland")
paleo_vars <- c("Length", "Width", "Thickness", "Mass")

# Olduvai: iterate over variables
results_olduvai <- list()
for (var in olduvai_vars) {
  values <- olduvai[[var]]
  values <- values[!is.na(values)]
  result <- OLE.test(values)  # Original function, unchanged
  results_olduvai[[var]] <- result
}

# Paleoindian: nested iteration over types and variables
results_paleo <- list()
for (type in paleo_types) {
  subset_data <- paleoindian[paleoindian$Type == type, ]
  for (var in paleo_vars) {
    values <- subset_data[[var]]
    values <- values[!is.na(values)]
    result <- OLE.test(values)
    results_paleo[[paste(type, var, sep = "_")]] <- result
  }
}

# Extract and save results
write.csv(do.call(rbind, results_olduvai), "outputs/table-5-results.csv")
write.csv(do.call(rbind, results_paleo), "outputs/table-6-results.csv")
```

This pattern preserves the original analysis function verbatim while parameterising the
iteration. The loop structure replaces manual re-execution with different variable
selections.

## Interactive Placeholder Substitution

Journal supplement scripts often use placeholder patterns for file paths that users
must replace manually before running:

```r
# Common patterns found in supplements:
data <- read.csv("###file location###")           # Key et al. 2024
source("C:/Users/Author/Desktop/functions.R")     # Hardcoded personal path
setwd("~/path/to/project")                        # Home directory reference
```

**Handling in wrapper scripts:**

1. Search for placeholder patterns: `###...###`, `TODO`, `CHANGE THIS`, `your path here`
2. Replace with relative paths appropriate for the Docker container
3. Replace `setwd()` calls with relative paths or `here::here()`
4. Document each substitution in the reproduction log

**Do NOT modify the analysis logic when substituting paths.** Path changes are
infrastructure, not analysis.

## Common Pitfalls

- **Changing `setwd()` paths** — Avoid hardcoded absolute paths. Use relative
  paths from the project root, or use `here::here()` for robust path
  resolution.
- **Missing `library()` calls** — When splitting code into functions or
  reorganising blocks, ensure all package dependencies are loaded before first
  use. The original script may rely on packages loaded earlier in an interactive
  session.
- **Forgetting to create output directories** — Add `dir.create("outputs",
  showWarnings = FALSE, recursive = TRUE)` before any file writes.
- **`print()` vs `ggsave()`** — ggplot objects need explicit `print()` inside
  loops and functions to render. In interactive mode, the REPL auto-prints; in
  batch mode, it does not.
- **Font dependencies** — Proprietary fonts (Gill Sans MT, Calibri, etc.) will
  not be available in Docker containers. Accept font substitution or install
  open-source alternatives (e.g., `fonts-liberation`). Do not let missing fonts
  block reproduction.
- **Empty supplement files** — Publishing errors can produce supplement files
  that are empty or contain only headers. Check file sizes before relying on
  supplement data (e.g., Key et al. 2024: mmc4.csv was 75 bytes, header only).
  Document as a publishing error, not a data availability issue.
- **Undocumented data preprocessing** — Original analyses may include data
  cleaning steps (duplicate removal, outlier filtering, unit conversion) that
  are not captured in the published scripts. If reproduced values include NaN
  or unexpected results, check whether the input data differs from what the
  original analysis used. Classify as CANNOT_COMPARE, not MAJOR_DISCREPANCY.
- **Supplement file naming** — Journal supplement numbering (mmc1, mmc2, etc.)
  may not correspond to the order referenced in the paper text. Verify which
  supplement file contains which script or data by examining content, not by
  relying on numbering alone.
