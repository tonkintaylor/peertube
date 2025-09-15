from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_video_captions_response_200 import GetVideoCaptionsResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID



def _get_kwargs(
    id: Union[UUID, int, str],
    *,
    x_peertube_video_password: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_peertube_video_password, Unset):
        headers["x-peertube-video-password"] = x_peertube_video_password



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/videos/{id}/captions".format(id=id,),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetVideoCaptionsResponse200]:
    if response.status_code == 200:
        response_200 = GetVideoCaptionsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetVideoCaptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Union[UUID, int, str],
    *,
    client: Union[AuthenticatedClient, Client],
    x_peertube_video_password: Union[Unset, str] = UNSET,

) -> Response[GetVideoCaptionsResponse200]:
    """ List captions of a video

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVideoCaptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
x_peertube_video_password=x_peertube_video_password,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: Union[UUID, int, str],
    *,
    client: Union[AuthenticatedClient, Client],
    x_peertube_video_password: Union[Unset, str] = UNSET,

) -> Optional[GetVideoCaptionsResponse200]:
    """ List captions of a video

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVideoCaptionsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
x_peertube_video_password=x_peertube_video_password,

    ).parsed

async def asyncio_detailed(
    id: Union[UUID, int, str],
    *,
    client: Union[AuthenticatedClient, Client],
    x_peertube_video_password: Union[Unset, str] = UNSET,

) -> Response[GetVideoCaptionsResponse200]:
    """ List captions of a video

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVideoCaptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
x_peertube_video_password=x_peertube_video_password,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: Union[UUID, int, str],
    *,
    client: Union[AuthenticatedClient, Client],
    x_peertube_video_password: Union[Unset, str] = UNSET,

) -> Optional[GetVideoCaptionsResponse200]:
    """ List captions of a video

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVideoCaptionsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
x_peertube_video_password=x_peertube_video_password,

    )).parsed
