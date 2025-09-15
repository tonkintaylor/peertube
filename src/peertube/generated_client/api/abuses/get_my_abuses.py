from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.abuse_state_set import AbuseStateSet
from ...models.get_my_abuses_sort import GetMyAbusesSort
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    id: Union[Unset, int] = UNSET,
    state: Union[Unset, AbuseStateSet] = UNSET,
    sort: Union[Unset, GetMyAbusesSort] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["id"] = id

    json_state: Union[Unset, int] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["start"] = start

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/abuses",
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
    id: Union[Unset, int] = UNSET,
    state: Union[Unset, AbuseStateSet] = UNSET,
    sort: Union[Unset, GetMyAbusesSort] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,

) -> Response[Any]:
    """ List my abuses

    Args:
        id (Union[Unset, int]):
        state (Union[Unset, AbuseStateSet]): The abuse state (Pending = `1`, Rejected = `2`,
            Accepted = `3`)
        sort (Union[Unset, GetMyAbusesSort]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
state=state,
sort=sort,
start=start,
count=count,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, int] = UNSET,
    state: Union[Unset, AbuseStateSet] = UNSET,
    sort: Union[Unset, GetMyAbusesSort] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,

) -> Response[Any]:
    """ List my abuses

    Args:
        id (Union[Unset, int]):
        state (Union[Unset, AbuseStateSet]): The abuse state (Pending = `1`, Rejected = `2`,
            Accepted = `3`)
        sort (Union[Unset, GetMyAbusesSort]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
state=state,
sort=sort,
start=start,
count=count,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

