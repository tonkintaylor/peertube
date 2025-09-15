from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.video_password_list import VideoPasswordList
from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID



def _get_kwargs(
    id: Union[UUID, int, str],
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/videos/{id}/passwords".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, VideoPasswordList]]:
    if response.status_code == 204:
        response_204 = VideoPasswordList.from_dict(response.json())



        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, VideoPasswordList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[Union[Any, VideoPasswordList]]:
    """ List video passwords

     **PeerTube >= 6.0**

    Args:
        id (Union[UUID, int, str]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VideoPasswordList]]
     """


    kwargs = _get_kwargs(
        id=id,
start=start,
count=count,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, VideoPasswordList]]:
    """ List video passwords

     **PeerTube >= 6.0**

    Args:
        id (Union[UUID, int, str]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VideoPasswordList]
     """


    return sync_detailed(
        id=id,
client=client,
start=start,
count=count,
sort=sort,

    ).parsed

async def asyncio_detailed(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[Union[Any, VideoPasswordList]]:
    """ List video passwords

     **PeerTube >= 6.0**

    Args:
        id (Union[UUID, int, str]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VideoPasswordList]]
     """


    kwargs = _get_kwargs(
        id=id,
start=start,
count=count,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, VideoPasswordList]]:
    """ List video passwords

     **PeerTube >= 6.0**

    Args:
        id (Union[UUID, int, str]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VideoPasswordList]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start=start,
count=count,
sort=sort,

    )).parsed
