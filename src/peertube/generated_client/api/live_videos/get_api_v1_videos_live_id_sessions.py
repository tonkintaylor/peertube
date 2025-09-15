from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_v1_videos_live_id_sessions_response_200 import GetApiV1VideosLiveIdSessionsResponse200
from typing import cast
from typing import cast, Union
from uuid import UUID



def _get_kwargs(
    id: Union[UUID, int, str],

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/videos/live/{id}/sessions".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetApiV1VideosLiveIdSessionsResponse200]:
    if response.status_code == 200:
        response_200 = GetApiV1VideosLiveIdSessionsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetApiV1VideosLiveIdSessionsResponse200]:
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

) -> Response[GetApiV1VideosLiveIdSessionsResponse200]:
    """ List live sessions

     List all sessions created in a particular live

    Args:
        id (Union[UUID, int, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1VideosLiveIdSessionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,

) -> Optional[GetApiV1VideosLiveIdSessionsResponse200]:
    """ List live sessions

     List all sessions created in a particular live

    Args:
        id (Union[UUID, int, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1VideosLiveIdSessionsResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,

) -> Response[GetApiV1VideosLiveIdSessionsResponse200]:
    """ List live sessions

     List all sessions created in a particular live

    Args:
        id (Union[UUID, int, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1VideosLiveIdSessionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: Union[UUID, int, str],
    *,
    client: AuthenticatedClient,

) -> Optional[GetApiV1VideosLiveIdSessionsResponse200]:
    """ List live sessions

     List all sessions created in a particular live

    Args:
        id (Union[UUID, int, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1VideosLiveIdSessionsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
