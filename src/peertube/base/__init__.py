"""Base classes and utilities for PeerTube API wrappers."""

from .client import PeerTubeClient, PeerTubeConfig
from .exceptions import AuthenticationError, NotFoundError, PeerTubeError
from .types import ApiResponse, AuthToken, PaginatedResponse, User, Video

# Export generated client access if available
try:
    from peertube.generated_client.peertube_client import (
        AuthenticatedClient as GeneratedAuthenticatedClient,
    )
    from peertube.generated_client.peertube_client import (
        Client as GeneratedClient,
    )

    __all__ = [
        "ApiResponse",
        "AuthToken",
        "AuthenticationError",
        "GeneratedAuthenticatedClient",
        "GeneratedClient",
        "NotFoundError",
        "PaginatedResponse",
        "PeerTubeClient",
        "PeerTubeConfig",
        "PeerTubeError",
        "User",
        "Video",
    ]
except ImportError:
    GeneratedClient = None
    GeneratedAuthenticatedClient = None
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
