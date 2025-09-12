"""Common types for PeerTube API wrappers."""

from typing import Any, Dict, Generic, Optional, TypeVar, Union
from pydantic import BaseModel, ConfigDict


T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Generic API response wrapper."""
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    data: T
    status_code: int
    headers: Dict[str, str] = {}


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated API response."""
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    data: list[T]
    total: int
    page: int
    per_page: int
    total_pages: int


class AuthToken(BaseModel):
    """Authentication token response."""
    
    access_token: str
    token_type: str = "Bearer"
    expires_in: Optional[int] = None
    refresh_token: Optional[str] = None


class User(BaseModel):
    """Basic user model."""
    
    id: int
    username: str
    email: Optional[str] = None
    display_name: Optional[str] = None
    role: str
    created_at: str
    updated_at: Optional[str] = None


class Video(BaseModel):
    """Basic video model."""
    
    id: int
    name: str
    description: Optional[str] = None
    duration: int
    views: int
    likes: int
    dislikes: int
    published_at: str
    created_at: str
    updated_at: Optional[str] = None