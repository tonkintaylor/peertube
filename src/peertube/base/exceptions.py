"""Custom exceptions for PeerTube API wrappers."""

from typing import Any


class PeerTubeError(Exception):
    """Base exception for PeerTube API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class AuthenticationError(PeerTubeError):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed") -> None:
        super().__init__(message, status_code=401)


class NotFoundError(PeerTubeError):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, status_code=404)


class ValidationError(PeerTubeError):
    """Raised when request validation fails."""

    def __init__(
        self,
        message: str = "Validation failed",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status_code=400, details=details)


class ForbiddenError(PeerTubeError):
    """Raised when access is forbidden."""

    def __init__(self, message: str = "Access forbidden") -> None:
        super().__init__(message, status_code=403)
