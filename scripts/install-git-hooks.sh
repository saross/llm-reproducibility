#!/bin/bash
# Install git hooks for llm-reproducibility repository
# Run this script after cloning the repository to enable local git hooks

set -e  # Exit on error

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "Installing git hooks..."
echo "Repository: $REPO_ROOT"
echo ""

# Check we're in a git repository
if [ ! -d "$REPO_ROOT/.git" ]; then
    echo "❌ ERROR: Not in a git repository"
    echo "Run this script from within the llm-reproducibility repository"
    exit 1
fi

# Create pre-commit hook
echo "Installing pre-commit hook (filename style enforcement)..."

cat > "$HOOKS_DIR/pre-commit" <<'EOF'
#!/bin/bash
# Pre-commit hook: Enforce lowercase-with-hyphens filename convention
# Per CLAUDE.md: "Use lowercase with hyphens for all filenames"
# Exceptions: README, CHANGELOG, CONTRIBUTING, CODE_OF_CONDUCT, CLAUDE, SKILL, LICENSE, CITATION

# Find ALL CAPS files in staged changes (excluding exceptions)
violations=$(git diff --cached --name-only --diff-filter=ACR | \
  grep -E '\.(md|py|json|yaml|yml|txt)$' | \
  grep -E '(^|/)[A-Z][A-Z_-]+\.(md|py|json|yaml|yml|txt)$' | \
  grep -v -E '(^|/)(README|CHANGELOG|CONTRIBUTING|CODE_OF_CONDUCT|CLAUDE|SKILL|CITATION|LICENSE)\.(md|txt)$')

if [ -n "$violations" ]; then
  echo ""
  echo "❌ ERROR: ALL CAPS filenames detected (violates CLAUDE.md file naming convention)"
  echo ""
  echo "Files with violations:"
  echo "$violations" | sed 's/^/  /'
  echo ""
  echo "Fix: Rename to lowercase-with-hyphens format"
  echo "  Example: MY_FILE.md → my-file.md"
  echo ""
  echo "Allowed exceptions (standard files only):"
  echo "  README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CLAUDE.md,"
  echo "  SKILL.md, LICENSE, CITATION.cff, CHANGELOG.md"
  echo ""
  exit 1
fi

# Success - allow commit
exit 0
EOF

chmod +x "$HOOKS_DIR/pre-commit"

echo "✅ pre-commit hook installed"
echo ""
echo "Git hooks installation complete!"
echo ""
echo "Installed hooks:"
echo "  - pre-commit: Filename style enforcement"
echo ""
echo "To bypass a hook (use sparingly):"
echo "  git commit --no-verify"
echo ""
