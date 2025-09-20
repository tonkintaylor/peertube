from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.types import Response


def _get_kwargs(registration_id: int) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/users/registrations/{registration_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    registration_id: int, *, client: AuthenticatedClient
) -> Response[Any]:
    """Delete registration
     Delete the registration entry. It will not remove the user associated with this registration (if
    any)

    Args:
        client: Authenticated HTTP client for API requests.
        registration_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(registration_id=registration_id)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(registration_id: int, *, client: AuthenticatedClient) -> Any | None:
    """Delete registration


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(registration_id=registration_id, client=client).parsed


async def asyncio_detailed(
    registration_id: int, *, client: AuthenticatedClient
) -> Response[Any]:
    """Delete registration
     Delete the registration entry. It will not remove the user associated with this registration (if
    any)

    Args:
        client: Authenticated HTTP client for API requests.
        registration_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(registration_id=registration_id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
