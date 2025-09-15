from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.block_status import BlockStatus
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    accounts: Union[Unset, list[str]] = UNSET,
    hosts: Union[Unset, list[str]] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_accounts: Union[Unset, list[str]] = UNSET
    if not isinstance(accounts, Unset):
        json_accounts = accounts


    params["accounts"] = json_accounts

    json_hosts: Union[Unset, list[str]] = UNSET
    if not isinstance(hosts, Unset):
        json_hosts = hosts


    params["hosts"] = json_hosts


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/blocklist/status",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BlockStatus]:
    if response.status_code == 200:
        response_200 = BlockStatus.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BlockStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    accounts: Union[Unset, list[str]] = UNSET,
    hosts: Union[Unset, list[str]] = UNSET,

) -> Response[BlockStatus]:
    """ Get block status of accounts/hosts

    Args:
        accounts (Union[Unset, list[str]]):
        hosts (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockStatus]
     """


    kwargs = _get_kwargs(
        accounts=accounts,
hosts=hosts,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    accounts: Union[Unset, list[str]] = UNSET,
    hosts: Union[Unset, list[str]] = UNSET,

) -> Optional[BlockStatus]:
    """ Get block status of accounts/hosts

    Args:
        accounts (Union[Unset, list[str]]):
        hosts (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockStatus
     """


    return sync_detailed(
        client=client,
accounts=accounts,
hosts=hosts,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    accounts: Union[Unset, list[str]] = UNSET,
    hosts: Union[Unset, list[str]] = UNSET,

) -> Response[BlockStatus]:
    """ Get block status of accounts/hosts

    Args:
        accounts (Union[Unset, list[str]]):
        hosts (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockStatus]
     """


    kwargs = _get_kwargs(
        accounts=accounts,
hosts=hosts,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    accounts: Union[Unset, list[str]] = UNSET,
    hosts: Union[Unset, list[str]] = UNSET,

) -> Optional[BlockStatus]:
    """ Get block status of accounts/hosts

    Args:
        accounts (Union[Unset, list[str]]):
        hosts (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockStatus
     """


    return (await asyncio_detailed(
        client=client,
accounts=accounts,
hosts=hosts,

    )).parsed
