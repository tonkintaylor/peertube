from typing import cast

from peertube.api.video_playlists.playlists import sync
from peertube.types import UNSET


class TestPlaylists:
    def test_sync(self, client, httpx_mock):
        # Mock the API response
        httpx_mock.add_response(
            method="GET",
            url="https://test.peertube.example/api/v1/video-playlists?count=15",
            json={
                "total": 2,
                "data": [
                    {
                        "id": 1,
                        "uuid": "12345678-1234-5678-1234-567812345678",
                        "url": "https://example.com/playlists/playlist-uuid-1",
                        "displayName": "My Playlist 1",
                        "shortDescription": "A short description",
                        "description": "A longer description",
                        "isLocal": True,
                        "ownerAccount": {
                            "id": 1,
                            "name": "@user@example.com",
                            "displayName": "User",
                            "url": "https://example.com/accounts/user",
                            "host": "example.com",
                            "avatar": None,
                        },
                        "createdAt": "2023-01-01T00:00:00.000Z",
                        "updatedAt": "2023-01-01T00:00:00.000Z",
                        "type": {"id": 1, "label": "Regular"},
                        "privacy": {"id": 1, "label": "Public"},
                        "videosLength": 5,
                        "thumbnailPath": "/static/thumbnails/playlists/"
                        "playlist-uuid-1.jpg",
                    },
                    {
                        "id": 2,
                        "uuid": "87654321-4321-8765-4321-876543218765",
                        "url": "https://example.com/playlists/playlist-uuid-2",
                        "displayName": "My Playlist 2",
                        "shortDescription": "Another short description",
                        "description": "Another longer description",
                        "isLocal": True,
                        "ownerAccount": {
                            "id": 1,
                            "name": "@user@example.com",
                            "displayName": "User",
                            "url": "https://example.com/accounts/user",
                            "host": "example.com",
                            "avatar": None,
                        },
                        "createdAt": "2023-01-02T00:00:00.000Z",
                        "updatedAt": "2023-01-02T00:00:00.000Z",
                        "type": {"id": 1, "label": "Regular"},
                        "privacy": {"id": 1, "label": "Public"},
                        "videosLength": 3,
                        "thumbnailPath": "/static/thumbnails/playlists/"
                        "playlist-uuid-2.jpg",
                    },
                ],
            },
            status_code=200,
        )

        # Call the sync function
        result = sync(client=client)

        # Assert the result
        assert result is not None
        assert result.total == 2
        assert result.data is not UNSET
        data = cast("list", result.data)
        assert len(data) == 2
        assert data[0].id == 1
        assert data[0].display_name == "My Playlist 1"
        assert data[1].id == 2
        assert data[1].display_name == "My Playlist 2"
