from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union



def _get_kwargs(
    *,
    search: Union[Unset, str] = UNSET,
    search_account: Union[Unset, str] = UNSET,
    search_video: Union[Unset, str] = UNSET,
    video_id: Union[Unset, int] = UNSET,
    video_channel_id: Union[Unset, int] = UNSET,
    auto_tag_one_of: Union[Unset, list[str], str] = UNSET,
    is_local: Union[Unset, bool] = UNSET,
    on_local_video: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["search"] = search

    params["searchAccount"] = search_account

    params["searchVideo"] = search_video

    params["videoId"] = video_id

    params["videoChannelId"] = video_channel_id

    json_auto_tag_one_of: Union[Unset, list[str], str]
    if isinstance(auto_tag_one_of, Unset):
        json_auto_tag_one_of = UNSET
    elif isinstance(auto_tag_one_of, list):
        json_auto_tag_one_of = auto_tag_one_of


    else:
        json_auto_tag_one_of = auto_tag_one_of
    params["autoTagOneOf"] = json_auto_tag_one_of

    params["isLocal"] = is_local

    params["onLocalVideo"] = on_local_video


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/videos/comments",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    search_account: Union[Unset, str] = UNSET,
    search_video: Union[Unset, str] = UNSET,
    video_id: Union[Unset, int] = UNSET,
    video_channel_id: Union[Unset, int] = UNSET,
    auto_tag_one_of: Union[Unset, list[str], str] = UNSET,
    is_local: Union[Unset, bool] = UNSET,
    on_local_video: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ List instance comments

    Args:
        search (Union[Unset, str]):
        search_account (Union[Unset, str]):
        search_video (Union[Unset, str]):
        video_id (Union[Unset, int]):
        video_channel_id (Union[Unset, int]):
        auto_tag_one_of (Union[Unset, list[str], str]):
        is_local (Union[Unset, bool]):
        on_local_video (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        search=search,
search_account=search_account,
search_video=search_video,
video_id=video_id,
video_channel_id=video_channel_id,
auto_tag_one_of=auto_tag_one_of,
is_local=is_local,
on_local_video=on_local_video,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: Union[Unset, str] = UNSET,
    search_account: Union[Unset, str] = UNSET,
    search_video: Union[Unset, str] = UNSET,
    video_id: Union[Unset, int] = UNSET,
    video_channel_id: Union[Unset, int] = UNSET,
    auto_tag_one_of: Union[Unset, list[str], str] = UNSET,
    is_local: Union[Unset, bool] = UNSET,
    on_local_video: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ List instance comments

    Args:
        search (Union[Unset, str]):
        search_account (Union[Unset, str]):
        search_video (Union[Unset, str]):
        video_id (Union[Unset, int]):
        video_channel_id (Union[Unset, int]):
        auto_tag_one_of (Union[Unset, list[str], str]):
        is_local (Union[Unset, bool]):
        on_local_video (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        search=search,
search_account=search_account,
search_video=search_video,
video_id=video_id,
video_channel_id=video_channel_id,
auto_tag_one_of=auto_tag_one_of,
is_local=is_local,
on_local_video=on_local_video,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

