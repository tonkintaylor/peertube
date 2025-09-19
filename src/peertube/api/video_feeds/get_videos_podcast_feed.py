from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.types import UNSET, Response


def _get_kwargs(
    *, video_channel_id: str) -> dict[str, Any]:
    params: dict[str, Any]={}

    params["videoChannelId"]=video_channel_id
    params={k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any]={
        "method": "get", "url": "/feeds/podcast/videos.xml", "params": params, }

    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code== 200:
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
    *, client: AuthenticatedClient | Client, video_channel_id: str) -> Response[Any]:
    """Videos podcast feed

    Args:
        video_channel_id (str): Video-related parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        video_channel_id = video_channel_id)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)


def sync(
    *, client: AuthenticatedClient | Client, video_channel_id: str) -> Any | None:
    """Videos podcast feed


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        client = client, video_channel_id = video_channel_id).parsed


async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, video_channel_id: str) -> Response[Any]:
    """Videos podcast feed

    Args:
        video_channel_id (str): Video-related parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        video_channel_id = video_channel_id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)
