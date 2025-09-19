from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.user_viewing_video import UserViewingVideo
from peertube.types import Response


def _get_kwargs(
    id: UUID | int | str, *, body: UserViewingVideo) -> dict[str, Any]:
    headers: dict[str, Any]={}

    _kwargs: dict[str, Any]={
        "method": "put", "url": f"/api/v1/videos/{id}/watching", }
    _kwargs["json"]=body.to_dict()

    headers["Content-Type"]="application/json"

    _kwargs["headers"]=headers
    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code== 204:
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
    id: UUID | int | str, *, client: AuthenticatedClient, body: UserViewingVideo) -> Response[Any]:
    """Set watching progress of a video

     This endpoint has been deprecated. Use `/videos/{id}/views` instead
    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.
        body (UserViewingVideo): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id, body = body)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)


def sync(
    id: UUID | int | str, *, client: AuthenticatedClient, body: UserViewingVideo) -> Any | None:
    """Set watching progress of a video


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        id = id, client = client, body = body).parsed


async def asyncio_detailed(
    id: UUID | int | str, *, client: AuthenticatedClient, body: UserViewingVideo) -> Response[Any]:
    """Set watching progress of a video

     This endpoint has been deprecated. Use `/videos/{id}/views` instead
    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.
        body (UserViewingVideo): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id = id, body = body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)
