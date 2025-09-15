from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.video_imports_list import VideoImportsList
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    target_url: Union[Unset, str] = UNSET,
    video_channel_sync_id: Union[Unset, float] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    params["sort"] = sort

    params["targetUrl"] = target_url

    params["videoChannelSyncId"] = video_channel_sync_id

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/videos/imports",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VideoImportsList]:
    if response.status_code == 200:
        response_200 = VideoImportsList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VideoImportsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    target_url: Union[Unset, str] = UNSET,
    video_channel_sync_id: Union[Unset, float] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Response[VideoImportsList]:
    """ Get video imports of my user

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        target_url (Union[Unset, str]):
        video_channel_sync_id (Union[Unset, float]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoImportsList]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
sort=sort,
target_url=target_url,
video_channel_sync_id=video_channel_sync_id,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    target_url: Union[Unset, str] = UNSET,
    video_channel_sync_id: Union[Unset, float] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Optional[VideoImportsList]:
    """ Get video imports of my user

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        target_url (Union[Unset, str]):
        video_channel_sync_id (Union[Unset, float]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoImportsList
     """


    return sync_detailed(
        client=client,
start=start,
count=count,
sort=sort,
target_url=target_url,
video_channel_sync_id=video_channel_sync_id,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    target_url: Union[Unset, str] = UNSET,
    video_channel_sync_id: Union[Unset, float] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Response[VideoImportsList]:
    """ Get video imports of my user

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        target_url (Union[Unset, str]):
        video_channel_sync_id (Union[Unset, float]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoImportsList]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
sort=sort,
target_url=target_url,
video_channel_sync_id=video_channel_sync_id,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    target_url: Union[Unset, str] = UNSET,
    video_channel_sync_id: Union[Unset, float] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Optional[VideoImportsList]:
    """ Get video imports of my user

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        target_url (Union[Unset, str]):
        video_channel_sync_id (Union[Unset, float]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoImportsList
     """


    return (await asyncio_detailed(
        client=client,
start=start,
count=count,
sort=sort,
target_url=target_url,
video_channel_sync_id=video_channel_sync_id,
search=search,

    )).parsed
