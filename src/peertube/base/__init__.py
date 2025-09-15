"""Base classes and utilities for PeerTube API wrappers."""

from .client import PeerTubeClient, PeerTubeConfig
from .exceptions import AuthenticationError, NotFoundError, PeerTubeError
from .types import ApiResponse, AuthToken, PaginatedResponse, User, Video

__all__ = [
    "ApiResponse",
    "AuthToken",
    "AuthenticationError",
    "NotFoundError",
    "PaginatedResponse",
    "PeerTubeClient",
    "PeerTubeConfig",
    "PeerTubeError",
    "User",
    "Video",
]
