"""Tests for search functionality."""

from unittest.mock import Mock, patch

from peertube.search import SearchClient, search_videos


def test_search_client_search_videos():
    """Test SearchClient search_videos functionality."""
    mock_client = Mock()
    mock_client.get.return_value = {
        "total": 1,
        "data": [
            {
                "id": "found_video",
                "name": "Found Video",
                "description": "A video found by search",
            }
        ],
    }

    search_client = SearchClient(mock_client)
    result = search_client.search_videos("test query")

    assert result["total"] == 1


def test_search_videos_convenience_function():
    """Test search_videos convenience function."""
    with patch("peertube.search.search.PeerTubeClient") as mock_client_class:
        mock_client = Mock()
        mock_client_class.return_value.__enter__.return_value = mock_client
        mock_client.get.return_value = {
            "total": 3,
            "data": [
                {"id": "video1"},
                {"id": "video2"},
                {"id": "video3"},
            ],
        }

        result = search_videos("https://example.com", "test search")

        assert result["total"] == 3
