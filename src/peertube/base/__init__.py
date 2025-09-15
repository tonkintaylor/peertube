"""Base classes and utilities for PeerTube API wrappers."""

from .client import PeerTubeClient, PeerTubeConfig
from .exceptions import AuthenticationError, NotFoundError, PeerTubeError
from .types import ApiResponse, AuthToken, PaginatedResponse, User, Video

# Export generated client access if available
try:
    from ..generated_client.peertube_client import (
        AuthenticatedClient as GeneratedAuthenticatedClient,
        Client as GeneratedClient,
    )
    _GENERATED_CLIENT_EXPORTS = [
        "GeneratedClient",
        "GeneratedAuthenticatedClient",
    ]
except ImportError:
    GeneratedClient = None
    GeneratedAuthenticatedClient = None
    _GENERATED_CLIENT_EXPORTS = []

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
    *_GENERATED_CLIENT_EXPORTS,
]
