"""Tests for video functionality."""

from unittest.mock import Mock, patch

from peertube.videos import VideoClient, get_video, list_videos


def test_video_client_get_video():
    """Test VideoClient get_video functionality."""
    mock_client = Mock()
    mock_client.get.return_value = {
        "id": "test_video_id",
        "name": "Test Video",
        "description": "A test video",
    }

    video_client = VideoClient(mock_client)
    result = video_client.get_video("test_video_id")

    assert result["id"] == "test_video_id"


def test_video_client_list_videos():
    """Test VideoClient list_videos functionality."""
    mock_client = Mock()
    mock_client.get.return_value = {
        "total": 1,
        "data": [
            {
                "id": "test_video_id",
                "name": "Test Video",
            }
        ],
    }

    video_client = VideoClient(mock_client)
    result = video_client.list_videos()

    assert result["total"] == 1


def test_get_video_convenience_function():
    """Test get_video convenience function."""
    with patch("peertube.videos.videos.PeerTubeClient") as mock_client_class:
        mock_client = Mock()
        mock_client_class.return_value.__enter__.return_value = mock_client
        mock_client.get.return_value = {
            "id": "convenience_video",
            "name": "Convenience Test",
        }

        result = get_video("https://example.com", "convenience_video")

        assert result["id"] == "convenience_video"


def test_list_videos_convenience_function():
    """Test list_videos convenience function."""
    with patch("peertube.videos.videos.PeerTubeClient") as mock_client_class:
        mock_client = Mock()
        mock_client_class.return_value.__enter__.return_value = mock_client
        mock_client.get.return_value = {
            "total": 2,
            "data": [{"id": "video1"}, {"id": "video2"}],
        }

        result = list_videos("https://example.com")

        assert result["total"] == 2
