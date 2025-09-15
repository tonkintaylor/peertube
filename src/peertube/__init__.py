"""Python API wrappers for PeerTube."""

__version__ = "0.1.0"

# Re-export main functionality for easy access
from .auth import (
    check_username_availability,
    get_user_info,
    login,
    logout,
    register_user,
)
from .base import (
    AuthenticationError,
    AuthToken,
    NotFoundError,
    PeerTubeClient,
    PeerTubeConfig,
    PeerTubeError,
    User,
    Video,
)
from .search import SearchClient, search_videos
from .videos import VideoClient, get_video, list_videos

__all__ = [
    "AuthToken",
    "AuthenticationError",
    "NotFoundError",
    "PeerTubeClient",
    "PeerTubeConfig",
    "PeerTubeError",
    "SearchClient",
    "User",
    "Video",
    "VideoClient",
    "check_username_availability",
    "get_user_info",
    "get_video",
    "list_videos",
    "login",
    "logout",
    "register_user",
    "search_videos",
]
