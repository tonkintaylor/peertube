"""Core video operations for PeerTube API.

This module provides wrapper functions for video-related API operations.
"""

from typing import Any, Dict

from ..base import PeerTubeClient


class VideoClient:
    """Client for video operations."""
    
    def __init__(self, client: PeerTubeClient):
        self.client = client
    
    def get_video(self, video_id: str) -> Dict[str, Any]:
        """Get video information by ID.
        
        Args:
            video_id: The video ID or UUID
            
        Returns:
            Video information as a dictionary
        """
        return self.client.get(f"/videos/{video_id}")
    
    def list_videos(
        self, 
        *, 
        start: int = 0, 
        count: int = 15,
        sort: str = "-publishedAt"
    ) -> Dict[str, Any]:
        """List videos with pagination.
        
        Args:
            start: Offset for pagination
            count: Number of items to return
            sort: Sort criteria
            
        Returns:
            Paginated video list
        """
        params = {
            "start": start,
            "count": count,
            "sort": sort,
        }
        return self.client.get("/videos", params=params)


# Convenience functions for direct use
def get_video(base_url: str, video_id: str, token: str | None = None) -> Dict[str, Any]:
    """Get video information.
    
    Args:
        base_url: PeerTube instance URL
        video_id: Video ID or UUID
        token: Optional authentication token
        
    Returns:
        Video information
    """
    from ..base import PeerTubeConfig
    
    config = PeerTubeConfig(base_url=base_url, token=token)
    with PeerTubeClient(config) as client:
        video_client = VideoClient(client)
        return video_client.get_video(video_id)


def list_videos(
    base_url: str, 
    *, 
    token: str | None = None,
    start: int = 0,
    count: int = 15,
    sort: str = "-publishedAt"
) -> Dict[str, Any]:
    """List videos from PeerTube instance.
    
    Args:
        base_url: PeerTube instance URL
        token: Optional authentication token
        start: Offset for pagination
        count: Number of items to return
        sort: Sort criteria
        
    Returns:
        Paginated video list
    """
    from ..base import PeerTubeConfig
    
    config = PeerTubeConfig(base_url=base_url, token=token)
    with PeerTubeClient(config) as client:
        video_client = VideoClient(client)
        return video_client.list_videos(start=start, count=count, sort=sort)


__all__ = [
    "VideoClient",
    "get_video",
    "list_videos",
]