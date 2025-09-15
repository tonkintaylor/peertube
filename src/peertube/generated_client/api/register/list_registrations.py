from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_registrations_response_200 import ListRegistrationsResponse200
from ...models.list_registrations_sort import ListRegistrationsSort
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListRegistrationsSort] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    params["search"] = search

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/registrations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ListRegistrationsResponse200]:
    if response.status_code == 200:
        response_200 = ListRegistrationsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ListRegistrationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListRegistrationsSort] = UNSET,

) -> Response[ListRegistrationsResponse200]:
    """ List registrations

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):
        sort (Union[Unset, ListRegistrationsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRegistrationsResponse200]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
search=search,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListRegistrationsSort] = UNSET,

) -> Optional[ListRegistrationsResponse200]:
    """ List registrations

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):
        sort (Union[Unset, ListRegistrationsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRegistrationsResponse200
     """


    return sync_detailed(
        client=client,
start=start,
count=count,
search=search,
sort=sort,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListRegistrationsSort] = UNSET,

) -> Response[ListRegistrationsResponse200]:
    """ List registrations

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):
        sort (Union[Unset, ListRegistrationsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRegistrationsResponse200]
     """


    kwargs = _get_kwargs(
        start=start,
count=count,
search=search,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, ListRegistrationsSort] = UNSET,

) -> Optional[ListRegistrationsResponse200]:
    """ List registrations

    Args:
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        search (Union[Unset, str]):
        sort (Union[Unset, ListRegistrationsSort]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRegistrationsResponse200
     """


    return (await asyncio_detailed(
        client=client,
start=start,
count=count,
search=search,
sort=sort,

    )).parsed
