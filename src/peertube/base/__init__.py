"""Base classes and utilities for PeerTube API wrappers."""

# Temporarily commenting out imports due to dependency issues
# from .client import PeerTubeClient, PeerTubeConfig
from .exceptions import PeerTubeError, AuthenticationError, NotFoundError
# from .types import ApiResponse

__all__ = [
    # "PeerTubeClient",
    # "PeerTubeConfig", 
    "PeerTubeError",
    "AuthenticationError",
    "NotFoundError",
    # "ApiResponse",
]