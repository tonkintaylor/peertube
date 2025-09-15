"""PeerTube generated client module.

This would contain the auto-generated client code from openapi-python-client.
For now, we provide a minimal implementation to support integration.
"""

from typing import Any, Dict

class Client:
    """Basic client structure for generated client integration."""
    
    def __init__(self, base_url: str, headers: Dict[str, str] | None = None):
        self.base_url = base_url
        self.headers = headers or {}

class AuthenticatedClient(Client):
    """Authenticated client for API operations requiring authentication."""
    
    def __init__(self, base_url: str, token: str, headers: Dict[str, str] | None = None):
        headers = headers or {}
        headers["Authorization"] = f"Bearer {token}"
        super().__init__(base_url, headers)


__all__ = ["Client", "AuthenticatedClient"]