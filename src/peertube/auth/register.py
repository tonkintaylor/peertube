"""User registration functionality."""

from typing import Dict, Any, Optional
from ..base import PeerTubeClient, PeerTubeConfig


class RegisterClient:
    """Client for user registration operations."""
    
    def __init__(self, config: PeerTubeConfig):
        self.config = config
        self._client = PeerTubeClient(config)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()
    
    def register(
        self,
        username: str,
        password: str,
        email: str,
        *,
        display_name: Optional[str] = None,
        channel_name: Optional[str] = None,
        channel_display_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Register a new user account."""
        data = {
            "username": username,
            "password": password,
            "email": email,
        }
        
        if display_name:
            data["displayName"] = display_name
        if channel_name:
            data["channel"] = {"name": channel_name}
            if channel_display_name:
                data["channel"]["displayName"] = channel_display_name
        
        return self._client.post("/users/register", json_data=data)
    
    def check_username_availability(self, username: str) -> Dict[str, Any]:
        """Check if a username is available for registration."""
        params = {"username": username}
        return self._client.get("/users/me/video-quota-used", params=params)


def register_user(
    base_url: str,
    username: str,
    password: str,
    email: str,
    *,
    display_name: Optional[str] = None,
    channel_name: Optional[str] = None,
    channel_display_name: Optional[str] = None,
    verify_ssl: bool = True
) -> Dict[str, Any]:
    """Convenience function to register a new user."""
    config = PeerTubeConfig(base_url=base_url, verify_ssl=verify_ssl)
    with RegisterClient(config) as client:
        return client.register(
            username=username,
            password=password,
            email=email,
            display_name=display_name,
            channel_name=channel_name,
            channel_display_name=channel_display_name
        )


def check_username_availability(base_url: str, username: str, *, verify_ssl: bool = True) -> Dict[str, Any]:
    """Convenience function to check username availability."""
    config = PeerTubeConfig(base_url=base_url, verify_ssl=verify_ssl)
    with RegisterClient(config) as client:
        return client.check_username_availability(username)