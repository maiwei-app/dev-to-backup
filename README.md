# Dev.to Backup

Automated backup of [Dev.to](https://dev.to/colomr) posts to GitHub.

## How it works

- **Monthly automated backups**: GitHub Actions runs on the first day of each month
- **Manual backups**: Trigger workflow manually anytime to backup new posts

## Structure

Posts are organized by year and month:

```
2026/
├── 08/
│   ├── august-monthly.md (automated backup)
│   ├── manual-1.md (manual backups)
│   └── manual-2.md
└── 09/
    └── september-monthly.md
```

Each file contains the post content in Markdown format with metadata.
