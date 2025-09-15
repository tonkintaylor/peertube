from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
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
        "url": "/api/v1/videos/{id}/description".format(id=id,),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[None, str]]:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[None, str]]:
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

) -> Response[Union[None, str]]:
    """ Get complete video description

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, str]]
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

) -> Optional[Union[None, str]]:
    """ Get complete video description

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, str]
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

) -> Response[Union[None, str]]:
    """ Get complete video description

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, str]]
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

) -> Optional[Union[None, str]]:
    """ Get complete video description

    Args:
        id (Union[UUID, int, str]):
        x_peertube_video_password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, str]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
x_peertube_video_password=x_peertube_video_password,

    )).parsed
