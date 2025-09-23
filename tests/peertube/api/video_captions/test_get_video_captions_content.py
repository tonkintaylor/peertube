"""Tests for get_video_captions_content function."""

from unittest.mock import Mock

import httpx
import pytest

from peertube.api.video_captions.get_video_captions_content import (
    get_video_captions_content,
)
from peertube.client import Client
from peertube.models.get_video_captions_response_200 import GetVideoCaptionsResponse200
from peertube.models.video_caption import VideoCaption
from peertube.models.video_constant_string_language import VideoConstantStringLanguage
from peertube.types import UNSET


@pytest.fixture
def mock_client():
    """Create a mock client."""
    client = Mock(spec=Client)
    client.base_url = "https://peertube.example.com"
    mock_httpx_client = Mock()
    client.get_httpx_client.return_value = mock_httpx_client
    return client


@pytest.fixture
def sample_vtt_content():
    """Sample VTT file content."""
    return """WEBVTT

00:00:00.000 --> 00:00:02.000
Hello world!

00:00:02.000 --> 00:00:04.000
This is a test caption.
"""


@pytest.fixture
def english_caption():
    """Create a sample English caption."""
    language = VideoConstantStringLanguage(id="en", label="English")
    caption = VideoCaption(
        language=language,
        caption_path="/api/v1/videos/test-video/captions/en"
    )
    caption.additional_properties = {"fileUrl": "https://peertube.example.com/caption/en.vtt"}
    return caption


@pytest.fixture
def french_caption():
    """Create a sample French caption."""
    language = VideoConstantStringLanguage(id="fr", label="French")
    caption = VideoCaption(
        language=language,
        caption_path="/api/v1/videos/test-video/captions/fr"
    )
    caption.additional_properties = {"fileUrl": "https://peertube.example.com/caption/fr.vtt"}
    return caption


@pytest.fixture
def captions_response_with_english(english_caption):
    """Create a captions response with English caption."""
    return GetVideoCaptionsResponse200(total=1, data=[english_caption])


@pytest.fixture
def captions_response_with_multiple(english_caption, french_caption):
    """Create a captions response with multiple captions."""
    return GetVideoCaptionsResponse200(total=2, data=[english_caption, french_caption])


class TestGetVideoCaptionsContentHappyPath:
    """Test happy path scenarios."""

    def test_get_captions_content_success(
        self, mocker, mock_client, captions_response_with_english, sample_vtt_content
    ):
        """Test successful caption content retrieval."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_english

        # Mock HTTP response
        mock_response = Mock()
        mock_response.content = sample_vtt_content.encode("utf-8")
        mock_response.raise_for_status.return_value = None
        mock_client.get_httpx_client().get.return_value = mock_response

        # Test the function
        result = get_video_captions_content(client=mock_client, id="test-video")

        assert result == sample_vtt_content


class TestGetVideoCaptionsContentLanguageFiltering:
    """Test language filtering scenarios."""

    def test_get_captions_specific_language(
        self, mocker, mock_client, captions_response_with_multiple, sample_vtt_content
    ):
        """Test retrieving captions for a specific language."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_multiple

        # Mock HTTP response
        mock_response = Mock()
        mock_response.content = sample_vtt_content.encode("utf-8")
        mock_response.raise_for_status.return_value = None
        mock_client.get_httpx_client().get.return_value = mock_response

        # Test with French language filter
        result = get_video_captions_content(
            client=mock_client, id="test-video", language_filter="fr"
        )

        # Should call HTTP GET with French caption URL
        mock_client.get_httpx_client().get.assert_called_once_with(
            "https://peertube.example.com/caption/fr.vtt"
        )
        assert result == sample_vtt_content

    def test_get_captions_no_language_filter(
        self, mocker, mock_client, captions_response_with_multiple, sample_vtt_content
    ):
        """Test retrieving captions without language filter uses first available."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_multiple

        # Mock HTTP response
        mock_response = Mock()
        mock_response.content = sample_vtt_content.encode("utf-8")
        mock_response.raise_for_status.return_value = None
        mock_client.get_httpx_client().get.return_value = mock_response

        # Test without language filter
        result = get_video_captions_content(
            client=mock_client, id="test-video", language_filter=None
        )

        # Should use first caption (English)
        mock_client.get_httpx_client().get.assert_called_once_with(
            "https://peertube.example.com/caption/en.vtt"
        )
        assert result == sample_vtt_content


class TestGetVideoCaptionsContentErrorCases:
    """Test error scenarios."""

    def test_no_captions_available(self, mocker, mock_client):
        """Test error when no captions are available."""
        # Mock get_video_captions_sync to return None
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = None

        with pytest.raises(ValueError, match="No captions available for this video"):
            get_video_captions_content(client=mock_client, id="test-video")

    def test_empty_captions_data(self, mocker, mock_client):
        """Test error when captions data is empty."""
        # Mock get_video_captions_sync to return empty data
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        empty_response = GetVideoCaptionsResponse200(total=0, data=[])
        mock_get_captions.return_value = empty_response

        with pytest.raises(ValueError, match="No captions available for this video"):
            get_video_captions_content(client=mock_client, id="test-video")

    def test_language_not_found(
        self, mocker, mock_client, captions_response_with_english
    ):
        """Test error when requested language is not found."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_english

        with pytest.raises(
            ValueError,
            match=r"Caption language 'de' not found\. Available languages: \['en'\]"
        ):
            get_video_captions_content(
                client=mock_client, id="test-video", language_filter="de"
            )

    def test_http_error_during_download(
        self, mocker, mock_client, captions_response_with_english
    ):
        """Test error handling for HTTP errors during download."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_english

        # Mock HTTP error
        mock_client.get_httpx_client().get.side_effect = httpx.HTTPError(
            "Network error"
        )

        with pytest.raises(httpx.HTTPError, match="Failed to download caption content"):
            get_video_captions_content(client=mock_client, id="test-video")

    def test_unicode_decode_error(
        self, mocker, mock_client, captions_response_with_english
    ):
        """Test error handling for Unicode decode errors."""
        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response_with_english

        # Mock response with invalid UTF-8 content
        mock_response = Mock()
        mock_response.content = b"\xff\xfe"  # Invalid UTF-8
        mock_response.raise_for_status.return_value = None
        mock_client.get_httpx_client().get.return_value = mock_response

        with pytest.raises(
            UnicodeDecodeError, match="Failed to decode caption content as UTF-8"
        ):
            get_video_captions_content(client=mock_client, id="test-video")


class TestGetVideoCaptionsContentUrlHandling:
    """Test URL handling scenarios."""

    def test_caption_path_relative_url(self, mocker, mock_client, sample_vtt_content):
        """Test handling of relative caption path URLs."""
        # Create caption with only caption_path (no fileUrl)
        language = VideoConstantStringLanguage(id="en", label="English")
        caption = VideoCaption(
            language=language,
            caption_path="/api/v1/videos/test-video/captions/en"
        )
        # No fileUrl in additional_properties
        captions_response = GetVideoCaptionsResponse200(total=1, data=[caption])

        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response

        # Mock HTTP response
        mock_response = Mock()
        mock_response.content = sample_vtt_content.encode("utf-8")
        mock_response.raise_for_status.return_value = None
        mock_client.get_httpx_client().get.return_value = mock_response

        # Test the function
        result = get_video_captions_content(client=mock_client, id="test-video")

        # Should construct full URL from relative path
        expected_url = "https://peertube.example.com/api/v1/videos/test-video/captions/en"
        mock_client.get_httpx_client().get.assert_called_once_with(expected_url)
        assert result == sample_vtt_content

    def test_no_caption_url_available(self, mocker, mock_client):
        """Test error when no caption URL is available."""
        # Create caption with no fileUrl and no caption_path
        language = VideoConstantStringLanguage(id="en", label="English")
        caption = VideoCaption(language=language, caption_path=UNSET)
        # No fileUrl in additional_properties
        captions_response = GetVideoCaptionsResponse200(total=1, data=[caption])

        # Mock get_video_captions_sync
        mock_get_captions = mocker.patch(
            "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
        )
        mock_get_captions.return_value = captions_response

        with pytest.raises(ValueError, match="Caption URL not found in response"):
            get_video_captions_content(client=mock_client, id="test-video")
