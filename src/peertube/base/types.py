"""Common types for PeerTube API wrappers."""

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Generic API response wrapper."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    data: T
    status_code: int
    headers: dict[str, str] = {}


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
    expires_in: int | None = None
    refresh_token: str | None = None


class User(BaseModel):
    """Basic user model."""

    id: int
    username: str
    email: str | None = None
    display_name: str | None = None
    role: str
    created_at: str
    updated_at: str | None = None


class Video(BaseModel):
    """Basic video model."""

    id: int
    name: str
    description: str | None = None
    duration: int
    views: int
    likes: int
    dislikes: int
    published_at: str
    created_at: str
    updated_at: str | None = None
