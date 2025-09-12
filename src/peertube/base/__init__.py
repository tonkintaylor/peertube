"""Base classes and utilities for PeerTube API wrappers."""

from .client import PeerTubeClient, PeerTubeConfig
from .exceptions import PeerTubeError, AuthenticationError, NotFoundError
from .types import ApiResponse, AuthToken, User, Video, PaginatedResponse

__all__ = [
    "PeerTubeClient",
    "PeerTubeConfig", 
    "PeerTubeError",
    "AuthenticationError",
    "NotFoundError",
    "ApiResponse",
    "AuthToken",
    "User", 
    "Video",
    "PaginatedResponse",
]