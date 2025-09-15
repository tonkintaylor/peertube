from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_channels_search_target import SearchChannelsSearchTarget
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    search: str,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search_target: Union[Unset, SearchChannelsSearchTarget] = UNSET,
    sort: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    handles: Union[Unset, Any] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["search"] = search

    params["start"] = start

    params["count"] = count

    json_search_target: Union[Unset, str] = UNSET
    if not isinstance(search_target, Unset):
        json_search_target = search_target.value

    params["searchTarget"] = json_search_target

    params["sort"] = sort

    params["host"] = host

    params["handles"] = handles


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/video-channels",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search_target: Union[Unset, SearchChannelsSearchTarget] = UNSET,
    sort: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    handles: Union[Unset, Any] = UNSET,

) -> Response[Any]:
    """ Search channels

    Args:
        search (str):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search_target (Union[Unset, SearchChannelsSearchTarget]):
        sort (Union[Unset, str]):  Example: -createdAt.
        host (Union[Unset, str]):
        handles (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        search=search,
start=start,
count=count,
search_target=search_target,
sort=sort,
host=host,
handles=handles,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search_target: Union[Unset, SearchChannelsSearchTarget] = UNSET,
    sort: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    handles: Union[Unset, Any] = UNSET,

) -> Response[Any]:
    """ Search channels

    Args:
        search (str):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search_target (Union[Unset, SearchChannelsSearchTarget]):
        sort (Union[Unset, str]):  Example: -createdAt.
        host (Union[Unset, str]):
        handles (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        search=search,
start=start,
count=count,
search_target=search_target,
sort=sort,
host=host,
handles=handles,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

