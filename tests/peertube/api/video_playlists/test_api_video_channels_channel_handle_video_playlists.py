"""Tests for api_video_channels_channel_handle_video_playlists function."""

from peertube.api.video_playlists.api_video_channels_channel_handle_video_playlists import (  # noqa: E501
    sync,
)
from peertube.models.get_api_v1_video_channels_channel_handle_video_playlists_response_200 import (  # noqa: E501
    GetApiV1VideoChannelsChannelHandleVideoPlaylistsResponse200,
)
from peertube.types import UNSET


def test_api_video_channels_channel_handle_video_playlists_success(httpx_mock, client):
    """Test successful retrieval of channel playlists."""
    # Mock response data
    response_data = {
        "total": 1,
        "data": [
            {
                "id": 123,
                "displayName": "Test Playlist",
                "description": "A test playlist",
                "privacy": {"id": 1, "label": "Public"},
                "type": {"id": 1, "label": "Regular"},
                "createdAt": "2023-01-01T00:00:00.000Z",
                "updatedAt": "2023-01-01T00:00:00.000Z",
            }
        ],
    }

    # Mock HTTP response
    httpx_mock.add_response(
        method="GET",
        url="https://test.peertube.example/api/v1/video-channels/test-channel/video-playlists?count=15",
        json=response_data,
        status_code=200,
    )

    # Test the function
    result = sync(
        channel_handle="test-channel",
        client=client,
        start=UNSET,
        count=15,
        sort=UNSET,
        playlist_type=UNSET,
    )

    # Assert result is the expected model
    expected = GetApiV1VideoChannelsChannelHandleVideoPlaylistsResponse200.from_dict(
        response_data
    )
    assert result == expected
