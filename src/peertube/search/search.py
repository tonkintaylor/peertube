"""Search functionality for PeerTube API.

This module provides wrapper functions for search-related operations.
"""

from typing import Any

from peertube.base import PeerTubeClient, PeerTubeConfig


class SearchClient:
    """Client for search operations."""

    def __init__(self, client: PeerTubeClient) -> None:
        self.client = client

    def search_videos(
        self,
        search: str,
        *,
        start: int = 0,
        count: int = 15,
        sort: str = "-publishedAt",
    ) -> dict[str, Any]:
        """Search for videos.

        Args:
            search: Search query
            start: Offset for pagination
            count: Number of items to return
            sort: Sort criteria

        Returns:
            Search results with pagination
        """
        params = {
            "search": search,
            "start": start,
            "count": count,
            "sort": sort,
        }
        return self.client.get("/search/videos", params=params)


# Convenience function for direct use
def search_videos(  # noqa: PLR0913
    base_url: str,
    search: str,
    *,
    token: str | None = None,
    start: int = 0,
    count: int = 15,
    sort: str = "-publishedAt",
) -> dict[str, Any]:
    """Search for videos on PeerTube instance.

    Args:
        base_url: PeerTube instance URL
        search: Search query
        token: Optional authentication token
        start: Offset for pagination
        count: Number of items to return
        sort: Sort criteria

    Returns:
        Search results
    """
    config = PeerTubeConfig(base_url=base_url, token=token)
    with PeerTubeClient(config) as client:
        search_client = SearchClient(client)
        return search_client.search_videos(
            search=search, start=start, count=count, sort=sort
        )


__all__ = [
    "SearchClient",
    "search_videos",
]
