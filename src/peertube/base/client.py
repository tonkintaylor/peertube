"""Core client classes for PeerTube API interactions."""

import types
from dataclasses import dataclass
from typing import Any

import httpx

from .exceptions import (
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    PeerTubeError,
    ValidationError,
)


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
        if response.status_code in {200, 201}:
            return response.json() if response.content else {}
        elif response.status_code == 204:
            return {}
        elif response.status_code == 400:
            error_data = response.json() if response.content else {}
            raise ValidationError(
                error_data.get("detail", "Validation failed"),
                details=error_data.get("invalid-params", {}),
            )
        elif response.status_code == 401:
            raise AuthenticationError
        elif response.status_code == 403:
            error_data = response.json() if response.content else {}
            raise ForbiddenError(error_data.get("detail", "Access forbidden"))
        elif response.status_code == 404:
            error_data = response.json() if response.content else {}
            raise NotFoundError(error_data.get("detail", "Resource not found"))
        else:
            error_data = response.json() if response.content else {}
            raise PeerTubeError(
                error_data.get("detail", f"HTTP {response.status_code}"),
                status_code=response.status_code,
                details=error_data,
            )

    def get(
        self, endpoint: str, params: dict[str, Any] | None = None
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
