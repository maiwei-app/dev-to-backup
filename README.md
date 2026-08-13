# Dev.to Backup

Automated backup of [Dev.to](https://dev.to/colomr) posts to GitHub.

## Overview

This repository automatically backs up published Dev.to posts as Markdown files. Posts are synced monthly on an automated schedule or manually on demand, preserving content, metadata, and formatting in version control.

## What it does

- **Fetches posts** from Dev.to API using your username and API key
- **Converts to Markdown** with full post metadata (title, tags, reading time, publication date)
- **Deduplicates** — skips unchanged posts (detected by comparing file content)
- **Organizes by date** — posts stored in `YYYY/MM/` directory structure
- **Handles errors gracefully** — continues on failed requests instead of crashing

## Workflows

### Automated Monthly Backup
Runs automatically on the 1st of each month at 00:00 UTC.

**Trigger:** Cron schedule  
**Runs:** `scripts/backup.py`  
**Commits:** New/updated posts to `main`

### Manual Backup
Trigger anytime from GitHub Actions UI.

**Trigger:** `workflow_dispatch`  
**Runs:** Same as automated  
**Use case:** Backup new posts immediately without waiting for monthly cycle

## Development

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install dev dependencies (testing, linting)
pip install -r requirements-dev.txt
```

### Configuration

Set environment variable:
```bash
export DEVTO_API_KEY="your_api_key_here"
```

Get your API key: https://dev.to/settings/account

### Running locally

```bash
# Backup a specific username's posts
python3 scripts/backup.py

# Or set API key inline
DEVTO_API_KEY=your_key python3 scripts/backup.py
```

## Testing

### Run all tests

```bash
pytest tests/ -v
```

### Run with coverage

```bash
pytest tests/ -v --cov=scripts --cov-fail-under=75
```

Coverage is enforced at 75% minimum.

### Specific test class

```bash
pytest tests/test_backup.py::TestFetchUserPosts -v
```

### Linting

```bash
# Check Python code style
ruff check scripts/ tests/
```

## CI/CD

This repository uses reusable workflows from `maiwei-app/workflows`:

- **`ci-python.yml`** — Lint + tests on every PR and push to `main`
  - Runs: ruff lint + pytest + JSON validation
  - Requires: 75% test coverage
  
- **`no-ai-attribution.yml`** — Enforces human authorship
  - Blocks commits attributed to AI
  - Required for all PRs

## File Structure

```
dev-to-backup/
├── scripts/
│   └── backup.py          # Main backup script
├── tests/
│   ├── test_backup.py     # Unit tests (27 tests)
│   └── __init__.py
├── .github/
│   └── workflows/
│       ├── backup.yml     # Monthly automated backup
│       └── ci.yml         # CI workflow (lint + test on PR)
├── requirements.txt       # Runtime dependencies
├── requirements-dev.txt   # Dev dependencies (pytest, ruff, etc)
└── README.md
```

## Organization Directory Structure

Posts are organized by year and month:

```
2026/
├── 08/
│   ├── august-monthly.md    (automated backup)
│   ├── manual-1.md          (manual backups)
│   └── manual-2.md
└── 09/
    └── september-monthly.md
```

Each file contains:
- Post title as H1 heading
- Metadata: publication date, reading time, tags
- Original post link
- Full post body in Markdown

## Contributing

1. Create a branch: `git checkout -b feat/your-feature`
2. Make changes and commit (authored as yourself, not AI)
3. Push and create a PR
4. Ensure all checks pass:
   - CI (lint + tests must pass)
   - No AI attribution check
5. Request review and await approval
6. Merge via GitHub (branch auto-deletes)

## License

GPL-3.0 — See LICENSE file
