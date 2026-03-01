# Print Statements Hook

A Python-based pre-commit hook that uses static analysis to detect and prevent `print()` statements from being committed to your codebase. 

Using `print()` for debugging is common, but leaving them in production code can lead to cluttered logs and potential information leaks. This hook helps you maintain clean code by catching them before they are committed.

## Features

- **Static Analysis**: Uses Python's built-in `ast` module to scan code without executing it.
- **Fast**: Scans files quickly, even in large projects.
- **Pre-commit Integration**: Easy to add to your existing `.pre-commit-config.yaml`.
- **Informative**: Points out the exact file, line, and column where the `print` statement was found.

## Installation

You can install the package from PyPI:

```bash
pip install print-statements-hook
```

Or install it locally for development or testing:

```bash
pip install .
```

## Usage

### As a Pre-commit Hook

Add the following to your `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/kuldeepmodh/print-statements-hook
    rev: v0.1.0  # Use the latest tag or commit hash
    hooks:
      - id: check-print-statements
```

Then run:

```bash
pre-commit install
```

### Manual Usage

You can also run the script manually on specific files or directories:

```bash
# Check specific files
check-print-statements file1.py file2.py

# Check current directory recursively
check-print-statements

# Exclude specific files or directories
check-print-statements --exclude tests --exclude some_legacy_file.py
```

## Development

### Running Tests

This project uses `pytest` for testing.

```bash
pip install pytest
PYTHONPATH=. pytest
```

## How It Works

The hook parses your Python files into an Abstract Syntax Tree (AST). It then walks through the tree looking for `Call` nodes where the function being called is named `print`. If any are found, it reports the location and exits with a non-zero status code, preventing the git commit.

## Versioning

This project follows [Semantic Versioning](https://semver.org/). You can check the installed version using:

```bash
check-print-statements --version
```

### Releasing New Versions

Versioning is automated using `bump-my-version` and GitHub Actions. To release a new version:

1. Use `bump-my-version` to bump the version (e.g., from `0.1.0` to `0.2.0`):
   ```bash
   # This will update all files, create a commit, and add a Git tag
   bump-my-version bump minor  # Use 'patch', 'minor', or 'major'
   ```
2. Push the commit and the tag to GitHub:
   ```bash
   git push origin main
   git push origin --tags
   ```

3. The GitHub Actions release workflow will automatically build the package, publish it to PyPI, and create a GitHub Release.

Users can then reference the new specific version tag in their `.pre-commit-config.yaml` or install the new version via `pip install --upgrade print-statements-hook`.

## License

MIT License. See [LICENSE](LICENSE) for details.
