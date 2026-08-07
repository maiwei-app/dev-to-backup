#!/usr/bin/env python3
"""Unit tests for Dev.to backup script."""

from unittest.mock import Mock, patch

import pytest

from scripts.backup import (
    fetch_post_details,
    fetch_user_posts,
    get_backup_filename,
    is_scheduled_run,
    post_to_markdown,
    save_posts,
)


@pytest.fixture
def mock_post():
    """Sample post from Dev.to API."""
    return {
        "id": 123,
        "title": "Test Post",
        "description": "A test post",
        "published_at": "2026-08-07T10:30:00Z",
        "url": "https://dev.to/colomr/test-post",
        "tag_list": ["test", "python"],
        "reading_time_minutes": 5,
    }


@pytest.fixture
def mock_post_details():
    """Full post details with body_markdown."""
    return {
        "id": 123,
        "title": "Test Post",
        "body_markdown": "# Test\n\nThis is a test post.",
        "published_at": "2026-08-07T10:30:00Z",
    }


class TestFetchUserPosts:
    @patch("scripts.backup.requests.get")
    def test_fetch_single_page(self, mock_get, mock_post):
        """Test fetching posts from a single page."""
        mock_response = Mock()
        mock_response.json.side_effect = [[mock_post], []]  # Posts then empty to exit loop
        mock_get.return_value = mock_response

        posts = fetch_user_posts("colomr")

        assert len(posts) == 1
        assert posts[0]["id"] == 123
        assert mock_get.call_count == 2  # Called once per page + once to detect empty

    @patch("scripts.backup.requests.get")
    def test_fetch_multiple_pages(self, mock_get, mock_post):
        """Test fetching posts across multiple pages."""
        mock_response = Mock()
        mock_response.json.side_effect = [
            [mock_post],  # Page 1
            [mock_post],  # Page 2
            [],  # Empty page (stop)
        ]
        mock_get.return_value = mock_response

        posts = fetch_user_posts("colomr")

        assert len(posts) == 2
        assert mock_get.call_count == 3

    @patch("scripts.backup.requests.get")
    def test_fetch_with_api_key(self, mock_get, mock_post):
        """Test API key is included in headers."""
        mock_response = Mock()
        mock_response.json.side_effect = [[mock_post], []]
        mock_get.return_value = mock_response

        fetch_user_posts("colomr", api_key="test-key")

        # Verify API key was passed in headers
        call_kwargs = mock_get.call_args_list[0][1]
        assert call_kwargs["headers"]["api-key"] == "test-key"


class TestFetchPostDetails:
    @patch("scripts.backup.requests.get")
    def test_fetch_full_post(self, mock_get, mock_post_details):
        """Test fetching full post details."""
        mock_response = Mock()
        mock_response.json.return_value = mock_post_details
        mock_get.return_value = mock_response

        details = fetch_post_details(123)

        assert details["body_markdown"] == "# Test\n\nThis is a test post."
        mock_get.assert_called_once()


class TestScheduledRun:
    def test_is_scheduled_when_schedule(self):
        """Test detection of scheduled run."""
        with patch.dict("os.environ", {"GITHUB_EVENT_NAME": "schedule"}):
            assert is_scheduled_run() is True

    def test_is_not_scheduled_when_manual(self):
        """Test detection of manual run."""
        with patch.dict("os.environ", {"GITHUB_EVENT_NAME": "workflow_dispatch"}):
            assert is_scheduled_run() is False


class TestGetBackupFilename:
    @patch("scripts.backup.is_scheduled_run")
    @patch("pathlib.Path.glob")
    def test_monthly_filename_scheduled(self, mock_glob, mock_scheduled, mock_post):
        """Test monthly filename for scheduled runs."""
        mock_scheduled.return_value = True
        mock_glob.return_value = []

        filename = get_backup_filename(mock_post)

        assert "august-monthly.md" in filename

    @patch("scripts.backup.is_scheduled_run")
    @patch("pathlib.Path.glob")
    def test_manual_filename_increment(self, mock_glob, mock_scheduled, mock_post):
        """Test manual filename increments correctly."""
        mock_scheduled.return_value = False
        # Mock glob to return Path-like objects with .name attribute
        mock_file1 = Mock()
        mock_file1.name = "manual-1.md"
        mock_file2 = Mock()
        mock_file2.name = "manual-2.md"
        mock_glob.return_value = [mock_file1, mock_file2]

        filename = get_backup_filename(mock_post)

        assert "manual-3.md" in filename


class TestPostToMarkdown:
    def test_markdown_with_full_details(self, mock_post, mock_post_details):
        """Test markdown conversion with full post details."""
        markdown = post_to_markdown(mock_post, mock_post_details)

        assert "# Test Post" in markdown
        assert "This is a test post." in markdown
        assert "https://dev.to/colomr/test-post" in markdown
        assert "#test" in markdown
        assert "#python" in markdown

    def test_markdown_without_details(self, mock_post):
        """Test markdown conversion without full details."""
        markdown = post_to_markdown(mock_post, None)

        assert "# Test Post" in markdown
        assert "A test post" in markdown
        assert "https://dev.to/colomr/test-post" in markdown

    def test_markdown_metadata(self, mock_post, mock_post_details):
        """Test markdown includes required metadata."""
        markdown = post_to_markdown(mock_post, mock_post_details)

        assert "**Published:** 2026-08-07" in markdown
        assert "**Reading time:** 5 min" in markdown


class TestSavePosts:
    @patch("scripts.backup.fetch_post_details")
    @patch("scripts.backup.post_to_markdown")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.exists")
    @patch("pathlib.Path.read_text")
    def test_save_new_post(
        self,
        mock_read,
        mock_exists,
        mock_write,
        mock_markdown,
        mock_fetch,
        mock_post,
        mock_post_details,
    ):
        """Test saving a new post."""
        mock_exists.return_value = False
        mock_markdown.return_value = "# Test"
        mock_fetch.return_value = mock_post_details

        saved = save_posts([mock_post])

        assert saved == 1
        mock_write.assert_called_once()

    @patch("scripts.backup.fetch_post_details")
    @patch("scripts.backup.post_to_markdown")
    @patch("pathlib.Path.exists")
    @patch("pathlib.Path.read_text")
    def test_skip_unchanged_post(
        self, mock_read, mock_exists, mock_markdown, mock_fetch, mock_post, mock_post_details
    ):
        """Test skipping unchanged posts."""
        mock_exists.return_value = True
        mock_read.return_value = "# Test"
        mock_markdown.return_value = "# Test"
        mock_fetch.return_value = mock_post_details

        saved = save_posts([mock_post])

        assert saved == 0

    @patch("scripts.backup.fetch_post_details")
    def test_handle_fetch_error(self, mock_fetch, mock_post):
        """Test graceful handling of fetch errors."""
        mock_fetch.side_effect = Exception("API error")

        with patch("scripts.backup.post_to_markdown") as mock_markdown, \
             patch("pathlib.Path.exists") as mock_exists, \
             patch("pathlib.Path.write_text"):
            mock_exists.return_value = False
            mock_markdown.return_value = "# Test"

            saved = save_posts([mock_post])

            # Should still save with fallback content
            assert saved == 1
