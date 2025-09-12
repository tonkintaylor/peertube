"""Python API wrappers for PeerTube."""

__version__ = "0.1.0"

# Re-export main functionality for easy access
# Temporarily commenting out client imports due to httpx dependency issues
# from .base import PeerTubeClient, PeerTubeConfig, PeerTubeError, AuthenticationError, NotFoundError
from .base import PeerTubeError, AuthenticationError, NotFoundError
# from .auth import login, logout, get_user_info, register_user, check_username_availability

# Keep the old hello_world function for backwards compatibility during transition
from .functions.hello_world import hello_world

__all__ = [
    # Core client and configuration (temporarily disabled)
    # "PeerTubeClient",
    # "PeerTubeConfig",
    # Exceptions
    "PeerTubeError", 
    "AuthenticationError",
    "NotFoundError",
    # Authentication functions (temporarily disabled)
    # "login",
    # "logout",
    # "get_user_info",
    # "register_user",
    # "check_username_availability",
    # Legacy function (will be removed later)
    "hello_world",
]
