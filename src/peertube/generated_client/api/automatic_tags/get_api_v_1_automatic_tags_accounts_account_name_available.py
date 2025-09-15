from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.automatic_tag_available import AutomaticTagAvailable
from typing import cast



def _get_kwargs(
    account_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/automatic-tags/accounts/{account_name}/available".format(account_name=account_name,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AutomaticTagAvailable]:
    if response.status_code == 200:
        response_200 = AutomaticTagAvailable.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AutomaticTagAvailable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[AutomaticTagAvailable]:
    """ Get account available auto tags

     **PeerTube >= 6.2**

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomaticTagAvailable]
     """


    kwargs = _get_kwargs(
        account_name=account_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Optional[AutomaticTagAvailable]:
    """ Get account available auto tags

     **PeerTube >= 6.2**

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomaticTagAvailable
     """


    return sync_detailed(
        account_name=account_name,
client=client,

    ).parsed

async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[AutomaticTagAvailable]:
    """ Get account available auto tags

     **PeerTube >= 6.2**

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomaticTagAvailable]
     """


    kwargs = _get_kwargs(
        account_name=account_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Optional[AutomaticTagAvailable]:
    """ Get account available auto tags

     **PeerTube >= 6.2**

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomaticTagAvailable
     """


    return (await asyncio_detailed(
        account_name=account_name,
client=client,

    )).parsed
