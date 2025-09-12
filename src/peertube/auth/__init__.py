"""Authentication and session management for PeerTube API."""

from .session import SessionClient, login, logout, get_user_info
from .register import RegisterClient, register_user, check_username_availability

__all__ = [
    "SessionClient",
    "login",
    "logout", 
    "get_user_info",
    "RegisterClient",
    "register_user",
    "check_username_availability",
]