"""Python API wrappers for PeerTube."""

__version__ = "0.1.0"

# Re-export main functionality for easy access
from .base import PeerTubeClient, PeerTubeConfig, PeerTubeError, AuthenticationError, NotFoundError, AuthToken, User, Video
from .auth import login, logout, get_user_info, register_user, check_username_availability

__all__ = [
    # Core client and configuration
    "PeerTubeClient",
    "PeerTubeConfig",
    # Exceptions
    "PeerTubeError", 
    "AuthenticationError",
    "NotFoundError",
    # Type models
    "AuthToken",
    "User",
    "Video",
    # Authentication functions
    "login",
    "logout",
    "get_user_info",
    "register_user",
    "check_username_availability",
]
