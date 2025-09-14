# CI: pass pre-commit gate before committing

## One-time setup
- Sync dependencies (uv):
  - `uv sync`
- Install the git hook:
  - `uv run pre-commit install` (or `pre-commit install` if pre-commit is on PATH)

## Before every commit (from repo root)
1) Auto-format fast path (optional, speeds things up)
- `uv run ruff format .`

2) Run all hooks and apply fixes
- `uv run pre-commit run --all-files`
- If it reports “files were modified by this hook”:
  - `git add -A`
  - `uv run pre-commit run --all-files`
- Repeat until pre-commit finishes with no modifications.

3) Run test suite and fix any failures
- `uv run python -m pytest tests/ -v` (or `python -m pytest tests/ -v` if uv unavailable)
- If tests fail, fix the issues before proceeding to commit
- Re-run tests until all pass

4) Commit
- `git commit -m "…"`

## CI/CD Pre-commit Hook Issues

**Important: Always run pre-commit hooks locally BEFORE committing to avoid CI failures.**

### Root Cause: Auto-formatting Hooks Modify Files During CI
- Pre-commit hooks like `uv-export` and `pyproject-fmt` modify files automatically during execution
- When these modifications happen in CI, the workflow detects uncommitted changes and fails
- **Critical issue**: The `uv-export` hook regenerates `requirements.txt` from `uv.lock` in a specific format with exact versions and hashes
- If `requirements.txt` was manually created or doesn't match the exact format that `uv export` produces, the hook will modify it

### Common Files Auto-Modified by Hooks:
1. **`requirements.txt`** (by uv-export hook): 
   - Regenerated from `uv.lock` with exact versions, hashes, and dependency comments
   - Must match the exact format produced by `uv export --no-default-groups -o requirements.txt`
2. **`pyproject.toml`** (by pyproject-fmt hook): 
   - Section ordering is automatically standardized
3. **`uv.lock`** (by uv-lock hook): 
   - Lockfile may be updated if dependencies change

### Solution Protocol:
1. **Always run pre-commit locally first**: `uv run pre-commit run --all-files`
2. **If files are modified**: Review changes, then `git add` the modified files
3. **Re-run pre-commit**: `uv run pre-commit run --all-files` until no modifications occur
4. **Then commit and push**: The files are now in the exact format CI expects

### Emergency Fix for CI Failures:
- If CI fails with "files were modified by this hook":
  1. Run `uv run pre-commit run --all-files` locally
  2. Add and commit any file modifications
  3. Push the corrected files to fix the CI workflow

---

# Before implementing a function: fetch fresh context with MCP tool `context7`

Always gather up-to-date docs before writing new code or using a new API.

## What to fetch with `context7`
- Package/API docs for every third‑party dependency you plan to call.
- Latest Python 3.12 syntax and typing features relevant to the change.

## How to use `context7`
- Invoke the MCP tool with clear, targeted queries and ask for official sources and version info.
- Example invocations (adapt to your client’s syntax):
  - `context7: docs package=requests topics=install,quickstart,api,examples`
  - `context7: python version=3.12 topic=typing changes summary for "<task>"`
  - `context7: python version=3.12 topic="pattern matching" examples minimal`

## Apply the results
- Prefer APIs shown as current/stable in the fetched docs.
- Conform examples to Python 3.12 syntax.
- If results conflict, choose the latest stable and note the source in the PR description.

## If `context7` is unavailable
- Retry once. If still unavailable, proceed only with well‑established APIs and add a PR note to re‑verify with `context7`.

---

# Comment policy: never use “TODO”

- Do not introduce “TODO” (or variants like “TO DO”, “ToDo”, “@todo”) anywhere:
  - Not in code comments, docstrings, notebooks, or commit messages.
- If follow‑up work is needed:
  - Open a GitHub issue and reference it without using the word “TODO”.
  - Preferred format in code/comments: `NOTE: see issue #123 for follow‑up rationale` or `FOLLOW‑UP: see issue #123`.

Quick self-check before committing:
- Search and remove any occurrences: `git grep -n -E '\bT[O0]\s?DO\b|@todo' || true`
- Then run: `uv run ruff format . && uv run pre-commit run --all-files`

---

## Function and Test Writing Guidelines

### Functions

- When writing functions, refrain from using try-except statements, unless necessary, as it bloats the code.

### Tests

- When writing tests, do not test for edge cases, unless instructed otherwise.
- When writing tests, write one test case per function with one assertion, assume happy path, unless instructed differently.
- **Never test scripts in the scripts folder or any other folder.** All tests must be placed in the `tests/` directory only.
- **Never write tests inside of scripts.** Scripts should contain executable code, not test functions or assertions.
- **The scripts folder should never be a place for tests.** Keep scripts and tests completely separate.

---
