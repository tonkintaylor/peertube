from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.types import Response


def _get_kwargs(
    id: int, token_session_id: int) -> dict[str, Any]:
    _kwargs: dict[str, Any]={
        "method": "get", "url": f"/api/v1/users/{id}/token-sessions/{token_session_id}/revoke", }

    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code== 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None

def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code = HTTPStatus(response.status_code), content = response.content, headers = response.headers, parsed = _parse_response(client = client, response = response))


def sync_detailed(
    id: int, token_session_id: int, *, client: AuthenticatedClient) -> Response[Any]:
    """List token sessions


    Args:
        id (int):  Example: 42.
        token_session_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id, token_session_id = token_session_id)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)


def sync(
    id: int, token_session_id: int, *, client: AuthenticatedClient) -> Any | None:
    """List token sessions


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        id = id, token_session_id = token_session_id, client = client).parsed


async def asyncio_detailed(
    id: int, token_session_id: int, *, client: AuthenticatedClient) -> Response[Any]:
    """List token sessions


    Args:
        id (int):  Example: 42.
        token_session_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id, token_session_id = token_session_id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)
