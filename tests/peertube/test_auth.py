"""Tests for authentication functionality."""

from unittest.mock import Mock, patch

from peertube.auth.session import SessionClient, login
from peertube.base import AuthToken, PeerTubeConfig


def test_session_client_login():
    """Test SessionClient login functionality."""
    config = PeerTubeConfig(base_url="https://example.com")

    with patch("peertube.auth.session.PeerTubeClient") as mock_client_class:
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        mock_client.post.return_value = {
            "access_token": "test_token_123",
            "token_type": "Bearer",
        }

        client = SessionClient(config)
        result = client.login("testuser", "testpass")

        assert result.access_token == "test_token_123"


def test_login_convenience_function():
    """Test login convenience function."""
    with patch("peertube.auth.session.SessionClient") as mock_session_class:
        mock_session = Mock()
        mock_session_class.return_value.__enter__.return_value = mock_session
        mock_session.login.return_value = AuthToken(
            access_token="convenience_token",  # noqa: S106
            token_type="Bearer",  # noqa: S106
        )

        result = login("https://example.com", "user", "pass")

        assert result.access_token == "convenience_token"
