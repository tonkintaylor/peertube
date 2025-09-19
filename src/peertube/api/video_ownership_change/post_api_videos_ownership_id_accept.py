from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.types import Response


def _get_kwargs(
    id: UUID | int | str) -> dict[str, Any]:
    _kwargs: dict[str, Any]={
        "method": "post", "url": f"/api/v1/videos/ownership/{id}/accept", }

    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code== 204:
        return None

    if response.status_code== 403:
        return None

    if response.status_code== 404:
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
    id: UUID | int | str, *, client: AuthenticatedClient) -> Response[Any]:
    """Accept ownership change request

    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)


def sync(
    id: UUID | int | str, *, client: AuthenticatedClient) -> Any | None:
    """Accept ownership change request


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        id = id, client = client).parsed


async def asyncio_detailed(
    id: UUID | int | str, *, client: AuthenticatedClient) -> Response[Any]:
    """Accept ownership change request

    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)
