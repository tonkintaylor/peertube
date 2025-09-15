from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_followers_response_200 import GetAccountFollowersResponse200
from ...models.get_account_followers_sort import GetAccountFollowersSort
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    name: str,
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, GetAccountFollowersSort] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{name}/followers".format(name=name,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetAccountFollowersResponse200]:
    if response.status_code == 200:
        response_200 = GetAccountFollowersResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetAccountFollowersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, GetAccountFollowersSort] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Response[GetAccountFollowersResponse200]:
    """ List followers of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, GetAccountFollowersSort]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountFollowersResponse200]
     """


    kwargs = _get_kwargs(
        name=name,
start=start,
count=count,
sort=sort,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, GetAccountFollowersSort] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Optional[GetAccountFollowersResponse200]:
    """ List followers of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, GetAccountFollowersSort]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountFollowersResponse200
     """


    return sync_detailed(
        name=name,
client=client,
start=start,
count=count,
sort=sort,
search=search,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, GetAccountFollowersSort] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Response[GetAccountFollowersResponse200]:
    """ List followers of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, GetAccountFollowersSort]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountFollowersResponse200]
     """


    kwargs = _get_kwargs(
        name=name,
start=start,
count=count,
sort=sort,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, GetAccountFollowersSort] = UNSET,
    search: Union[Unset, str] = UNSET,

) -> Optional[GetAccountFollowersResponse200]:
    """ List followers of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, GetAccountFollowersSort]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountFollowersResponse200
     """


    return (await asyncio_detailed(
        name=name,
client=client,
start=start,
count=count,
sort=sort,
search=search,

    )).parsed
