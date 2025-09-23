"""Tests for get_video_captions_content function."""

from unittest.mock import Mock

from peertube.api.video_captions.get_video_captions_content import (
    get_video_captions_content,
)
from peertube.client import Client
from peertube.models.get_video_captions_response_200 import GetVideoCaptionsResponse200
from peertube.models.video_caption import VideoCaption
from peertube.models.video_constant_string_language import VideoConstantStringLanguage


def test_get_captions_content_success(mocker):
    """Test successful caption content retrieval."""
    # Mock client
    client = Mock(spec=Client)
    client.base_url = "https://peertube.example.com"
    mock_httpx_client = Mock()
    client.get_httpx_client.return_value = mock_httpx_client

    # Mock caption data
    language = VideoConstantStringLanguage(id="en", label="English")
    caption = VideoCaption(
        language=language,
        caption_path="/api/v1/videos/test-video/captions/en"
    )
    caption.additional_properties = {"fileUrl": "https://peertube.example.com/caption/en.vtt"}
    captions_response = GetVideoCaptionsResponse200(total=1, data=[caption])

    # Mock get_video_captions_sync
    mock_get_captions = mocker.patch(
        "peertube.api.video_captions.get_video_captions_content.get_video_captions_sync"
    )
    mock_get_captions.return_value = captions_response

    # Mock HTTP response
    sample_vtt_content = """WEBVTT

00:00:00.000 --> 00:00:02.000
Hello world!

00:00:02.000 --> 00:00:04.000
This is a test caption.
"""
    mock_response = Mock()
    mock_response.content = sample_vtt_content.encode("utf-8")
    mock_response.raise_for_status.return_value = None
    mock_httpx_client.get.return_value = mock_response

    # Test the function
    result = get_video_captions_content(client=client, id="test-video")

    assert result == sample_vtt_content
