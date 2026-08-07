#!/usr/bin/env python3
"""Backup Dev.to posts to GitHub repository.

Fetches posts from Dev.to API and saves them organized by year/month.
Automatically categorizes as 'monthly' for scheduled runs or requires
manual naming for manual triggers.
"""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

import requests

DEVTO_API_KEY = os.getenv("DEVTO_API_KEY", "")
DEVTO_USERNAME = "colomr"
DEVTO_BASE_URL = "https://dev.to/api"
REPO_ROOT = Path(__file__).parent.parent


def fetch_user_posts(username: str, api_key: str = "") -> list[dict]:
    """Fetch all published posts for a user from Dev.to API."""
    url = f"{DEVTO_BASE_URL}/articles"
    headers = {}
    if api_key:
        headers["api-key"] = api_key

    all_posts = []
    page = 1

    while True:
        params = {
            "username": username,
            "per_page": 50,
            "page": page,
            "state": "published",
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        posts = response.json()
        if not posts:
            break

        all_posts.extend(posts)
        page += 1

    return all_posts


def fetch_post_details(post_id: int, api_key: str = "") -> dict:
    """Fetch full post details including body_markdown."""
    url = f"{DEVTO_BASE_URL}/articles/{post_id}"
    headers = {}
    if api_key:
        headers["api-key"] = api_key

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def is_scheduled_run() -> bool:
    """Check if this is a scheduled run (vs manual trigger)."""
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    return event_name == "schedule"


def get_backup_filename(post: dict) -> str:
    """Generate filename for the post based on run type."""
    published_date = datetime.fromisoformat(
        post["published_at"].replace("Z", "+00:00")
    )
    year = published_date.strftime("%Y")
    month = published_date.strftime("%m")
    day_dir = REPO_ROOT / year / month

    day_dir.mkdir(parents=True, exist_ok=True)

    if is_scheduled_run():
        month_name = published_date.strftime("%B").lower()
        filename = f"{month_name}-monthly.md"
    else:
        # Find next available manual backup number
        existing = sorted(
            [f.name for f in day_dir.glob("manual-*.md")],
            key=lambda x: int(x.split("-")[1].split(".")[0]),
        )
        next_num = int(existing[-1].split("-")[1].split(".")[0]) + 1 if existing else 1
        filename = f"manual-{next_num}.md"

    return str(day_dir / filename)


def post_to_markdown(post: dict, details: dict = None) -> str:
    """Convert Dev.to post to Markdown format with metadata."""
    published = datetime.fromisoformat(
        post["published_at"].replace("Z", "+00:00")
    ).strftime("%Y-%m-%d")

    # Use full details if available, otherwise fall back to summary
    content = details.get("body_markdown", "") if details else ""
    if not content:
        content = f"*{post.get('description', 'No description available')}*"

    markdown = f"""# {post['title']}

**Published:** {published}
**URL:** {post['url']}
**Tags:** {', '.join(f'#{tag}' for tag in post.get('tag_list', []))}
**Reading time:** {post.get('reading_time_minutes', '?')} min

---

{content}
"""
    return markdown


def save_posts(posts: list[dict], api_key: str = "") -> int:
    """Save posts to files and return count of new/modified posts."""
    saved_count = 0

    for post in posts:
        try:
            # Try to fetch full post details
            details = fetch_post_details(post["id"], api_key)
        except Exception as e:
            print(f"Warning: Could not fetch full details for post {post['id']}: {e}")
            details = None

        filepath = get_backup_filename(post)
        content = post_to_markdown(post, details)

        path_obj = Path(filepath)
        if not path_obj.exists() or path_obj.read_text() != content:
            path_obj.write_text(content, encoding="utf-8")
            saved_count += 1

    return saved_count


def main():
    """Main backup routine."""
    try:
        posts = fetch_user_posts(DEVTO_USERNAME, DEVTO_API_KEY)
        print(f"Fetched {len(posts)} posts from Dev.to")

        saved = save_posts(posts, DEVTO_API_KEY)
        print(f"Saved {saved} new or modified posts")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=__import__("sys").stderr)
        return 1


if __name__ == "__main__":
    exit(main())
