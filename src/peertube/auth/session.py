"""Session management and login/logout functionality."""

from typing import Dict, Any
from ..base import PeerTubeClient, PeerTubeConfig, AuthToken, User


class SessionClient:
    """Client for managing user sessions and authentication."""
    
    def __init__(self, config: PeerTubeConfig):
        self.config = config
        self._client = PeerTubeClient(config)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()
    
    def login(self, username: str, password: str) -> AuthToken:
        """Login with username and password to get access token."""
        data = {
            "client_id": "local",
            "client_secret": "",
            "grant_type": "password",
            "response_type": "code",
            "username": username,
            "password": password,
        }
        
        response = self._client.post("/users/token", data=data)
        return AuthToken(**response)
    
    def logout(self) -> Dict[str, Any]:
        """Logout current session (revoke token)."""
        return self._client.post("/users/revoke-token")
    
    def get_user_info(self) -> User:
        """Get current user information."""
        response = self._client.get("/users/me")
        return User(**response)


def login(base_url: str, username: str, password: str, *, verify_ssl: bool = True) -> AuthToken:
    """Convenience function to login and get access token."""
    config = PeerTubeConfig(base_url=base_url, verify_ssl=verify_ssl)
    with SessionClient(config) as client:
        return client.login(username, password)


def logout(base_url: str, token: str, *, verify_ssl: bool = True) -> Dict[str, Any]:
    """Convenience function to logout and revoke token."""
    config = PeerTubeConfig(base_url=base_url, token=token, verify_ssl=verify_ssl)
    with SessionClient(config) as client:
        return client.logout()


def get_user_info(base_url: str, token: str, *, verify_ssl: bool = True) -> User:
    """Convenience function to get current user information."""
    config = PeerTubeConfig(base_url=base_url, token=token, verify_ssl=verify_ssl)
    with SessionClient(config) as client:
        return client.get_user_info()