# Compare every package in renv.lock with the version installed in the probe
# image's project library, and record the R runtime against the lockfile's.
lock <- jsonlite::fromJSON("renv.lock", simplifyVector = FALSE)
pk <- lock$Packages
# packageDescription keeps the version as written ("0.2-20"); compare as versions.
inst <- function(p) tryCatch(utils::packageDescription(p)$Version, error = function(e) NA_character_)
inv <- data.frame(package = names(pk),
                  locked = vapply(pk, function(x) x$Version, character(1)),
                  installed = vapply(names(pk), inst, character(1)))
inv$match <- !is.na(inv$installed) &
  mapply(function(a, b) !is.na(a) && package_version(a) == package_version(b),
         inv$installed, inv$locked)
write.csv(inv, "/out/lockfile-inventory.csv", row.names = FALSE)
cat("R running:", as.character(getRversion()), " lockfile R:", lock$R$Version, "\n")
cat("packages in lockfile:", nrow(inv), " installed at the locked version:", sum(inv$match), "\n")
print(inv[!inv$match, ])
