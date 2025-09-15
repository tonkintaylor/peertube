"""Core client classes for PeerTube API interactions."""

import types
from dataclasses import dataclass
from typing import Any

import httpx
from httpx import codes

from .exceptions import (
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    PeerTubeError,
    ValidationError,
)

# Import generated client if available
try:
    from peertube.generated_client.peertube_client import (
        AuthenticatedClient as GeneratedAuthenticatedClient,
    )
    from peertube.generated_client.peertube_client import (
        Client as GeneratedClient,
    )

    _GENERATED_CLIENT_AVAILABLE = True
except ImportError:
    _GENERATED_CLIENT_AVAILABLE = False
    GeneratedClient = None
    GeneratedAuthenticatedClient = None


@dataclass
class PeerTubeConfig:
    """Configuration for PeerTube client."""

    base_url: str
    token: str | None = None
    verify_ssl: bool = True
    timeout: int = 30

    def __post_init__(self) -> None:
        # Ensure base_url doesn't end with a slash
        if self.base_url.endswith("/"):
            self.base_url = self.base_url.rstrip("/")


class PeerTubeClient:
    """Base client for PeerTube API interactions."""

    def __init__(self, config: PeerTubeConfig) -> None:
        self.config = config
        self._http_client = httpx.Client(
            base_url=f"{config.base_url}/api/v1",
            timeout=config.timeout,
            verify=config.verify_ssl,
        )

        # Set authorization header if token is provided
        if config.token:
            self._http_client.headers["Authorization"] = f"Bearer {config.token}"

        # Initialize generated client if available
        self._generated_client = None
        if _GENERATED_CLIENT_AVAILABLE:
            try:
                if config.token:
                    self._generated_client = GeneratedAuthenticatedClient(
                        base_url=config.base_url,
                        token=config.token,
                    )
                else:
                    self._generated_client = GeneratedClient(base_url=config.base_url)
            except ImportError:
                # Fallback to manual client if generated client fails
                pass

    @property
    def generated_client(self) -> Any | None:
        """Access to the generated OpenAPI client if available."""
        return self._generated_client

    def __enter__(self) -> "PeerTubeClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._http_client.close()

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Handle HTTP response and raise appropriate exceptions."""
        if response.status_code in {codes.OK, codes.CREATED}:
            return response.json() if response.content else {}
        if response.status_code == codes.NO_CONTENT:
            return {}

        # Handle error responses
        error_data = response.json() if response.content else {}
        return self._handle_error_response(response.status_code, error_data)

    def _handle_error_response(
        self, status_code: int, error_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Handle error response status codes."""
        if status_code == codes.BAD_REQUEST:
            raise ValidationError(
                error_data.get("detail", "Validation failed"),
                details=error_data.get("invalid-params", {}),
            )
        elif status_code == codes.UNAUTHORIZED:
            raise AuthenticationError
        elif status_code == codes.FORBIDDEN:
            raise ForbiddenError(error_data.get("detail", "Access forbidden"))
        elif status_code == codes.NOT_FOUND:
            raise NotFoundError(error_data.get("detail", "Resource not found"))
        else:
            raise PeerTubeError(
                error_data.get("detail", f"HTTP {status_code}"),
                status_code=status_code,
                details=error_data,
            )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a GET request."""
        response = self._http_client.get(endpoint, params=params)
        return self._handle_response(response)

    def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a POST request."""
        response = self._http_client.post(endpoint, data=data, json=json_data)
        return self._handle_response(response)

    def put(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a PUT request."""
        response = self._http_client.put(endpoint, data=data, json=json_data)
        return self._handle_response(response)

    def delete(self, endpoint: str) -> dict[str, Any]:
        """Make a DELETE request."""
        response = self._http_client.delete(endpoint)
        return self._handle_response(response)
