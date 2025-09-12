"""Custom exceptions for PeerTube API wrappers."""

from typing import Any, Dict, Optional


class PeerTubeError(Exception):
    """Base exception for PeerTube API errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class AuthenticationError(PeerTubeError):
    """Raised when authentication fails."""
    
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message, status_code=401)


class NotFoundError(PeerTubeError):
    """Raised when a resource is not found."""
    
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ValidationError(PeerTubeError):
    """Raised when request validation fails."""
    
    def __init__(self, message: str = "Validation failed", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=400, details=details)


class ForbiddenError(PeerTubeError):
    """Raised when access is forbidden."""
    
    def __init__(self, message: str = "Access forbidden"):
        super().__init__(message, status_code=403)