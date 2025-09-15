from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.video_list_response import VideoListResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/history/videos",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VideoListResponse]:
    if response.status_code == 200:
        response_200 = VideoListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VideoListResponse]:
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
    search: Union[Unset, str] = UNSET,

) -> Response[VideoListResponse]:
    """ List watched videos history

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoListResponse]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
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
    search: Union[Unset, str] = UNSET,

) -> Optional[VideoListResponse]:
    """ List watched videos history

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoListResponse
     """


    return sync_detailed(
        client=client,
start=start,
count=count,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,

) -> Response[VideoListResponse]:
    """ List watched videos history

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoListResponse]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
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
    search: Union[Unset, str] = UNSET,

) -> Optional[VideoListResponse]:
    """ List watched videos history

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoListResponse
     """


    return (await asyncio_detailed(
        client=client,
start=start,
count=count,
search=search,

    )).parsed
