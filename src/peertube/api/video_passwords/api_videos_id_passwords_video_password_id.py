from typing import Any
from uuid import UUID

import httpx
from pydantic import ConfigDict, validate_call

from peertube import errors
from peertube.api.shared_utils import build_response
from peertube.client import AuthenticatedClient, Client
from peertube.types import Response


def _get_kwargs(id: UUID | int | str, video_password_id: int) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/videos/{id}/passwords/{video_password_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return build_response(client=client, response=response)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def sync_detailed(
    id: UUID | int | str, video_password_id: int, *, client: AuthenticatedClient
) -> Response[Any]:
    """Delete a video password

     **PeerTube > = 6.0**
    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.
        video_password_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(id=id, video_password_id=video_password_id)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def sync(
    id: UUID | int | str, video_password_id: int, *, client: AuthenticatedClient
) -> Any | None:
    """Delete a video password


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        id=id, video_password_id=video_password_id, client=client
    ).parsed


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
async def asyncio_detailed(
    id: UUID | int | str, video_password_id: int, *, client: AuthenticatedClient
) -> Response[Any]:
    """Delete a video password

     **PeerTube > = 6.0**
    Args:
        id (Union[UUID, int, str]): Unique identifier for the entity.
        video_password_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(id=id, video_password_id=video_password_id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
