from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_latest_user_import_response_200 import GetLatestUserImportResponse200
from typing import cast



def _get_kwargs(
    user_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/{user_id}/imports/latest".format(user_id=user_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetLatestUserImportResponse200]:
    if response.status_code == 200:
        response_200 = GetLatestUserImportResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetLatestUserImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetLatestUserImportResponse200]:
    """ Get latest user import

     **PeerTube >= 6.1**

    Args:
        user_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLatestUserImportResponse200]
     """


    kwargs = _get_kwargs(
        user_id=user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[GetLatestUserImportResponse200]:
    """ Get latest user import

     **PeerTube >= 6.1**

    Args:
        user_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLatestUserImportResponse200
     """


    return sync_detailed(
        user_id=user_id,
client=client,

    ).parsed

async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetLatestUserImportResponse200]:
    """ Get latest user import

     **PeerTube >= 6.1**

    Args:
        user_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLatestUserImportResponse200]
     """


    kwargs = _get_kwargs(
        user_id=user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,

) -> Optional[GetLatestUserImportResponse200]:
    """ Get latest user import

     **PeerTube >= 6.1**

    Args:
        user_id (int):  Example: 42.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLatestUserImportResponse200
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,

    )).parsed
