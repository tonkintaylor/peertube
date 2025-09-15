from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_v1_server_followers_actor_type import GetApiV1ServerFollowersActorType
from ...models.get_api_v1_server_followers_response_200 import GetApiV1ServerFollowersResponse200
from ...models.get_api_v1_server_followers_state import GetApiV1ServerFollowersState
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    state: Union[Unset, GetApiV1ServerFollowersState] = UNSET,
    actor_type: Union[Unset, GetApiV1ServerFollowersActorType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_actor_type: Union[Unset, str] = UNSET
    if not isinstance(actor_type, Unset):
        json_actor_type = actor_type.value

    params["actorType"] = json_actor_type

    params["start"] = start

    params["count"] = count

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/server/followers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetApiV1ServerFollowersResponse200]:
    if response.status_code == 200:
        response_200 = GetApiV1ServerFollowersResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetApiV1ServerFollowersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, GetApiV1ServerFollowersState] = UNSET,
    actor_type: Union[Unset, GetApiV1ServerFollowersActorType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[GetApiV1ServerFollowersResponse200]:
    """ List instances following the server

    Args:
        state (Union[Unset, GetApiV1ServerFollowersState]):
        actor_type (Union[Unset, GetApiV1ServerFollowersActorType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1ServerFollowersResponse200]
     """


    kwargs = _get_kwargs(
        state=state,
actor_type=actor_type,
start=start,
count=count,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, GetApiV1ServerFollowersState] = UNSET,
    actor_type: Union[Unset, GetApiV1ServerFollowersActorType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[GetApiV1ServerFollowersResponse200]:
    """ List instances following the server

    Args:
        state (Union[Unset, GetApiV1ServerFollowersState]):
        actor_type (Union[Unset, GetApiV1ServerFollowersActorType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1ServerFollowersResponse200
     """


    return sync_detailed(
        client=client,
state=state,
actor_type=actor_type,
start=start,
count=count,
sort=sort,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, GetApiV1ServerFollowersState] = UNSET,
    actor_type: Union[Unset, GetApiV1ServerFollowersActorType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[GetApiV1ServerFollowersResponse200]:
    """ List instances following the server

    Args:
        state (Union[Unset, GetApiV1ServerFollowersState]):
        actor_type (Union[Unset, GetApiV1ServerFollowersActorType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1ServerFollowersResponse200]
     """


    kwargs = _get_kwargs(
        state=state,
actor_type=actor_type,
start=start,
count=count,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, GetApiV1ServerFollowersState] = UNSET,
    actor_type: Union[Unset, GetApiV1ServerFollowersActorType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[GetApiV1ServerFollowersResponse200]:
    """ List instances following the server

    Args:
        state (Union[Unset, GetApiV1ServerFollowersState]):
        actor_type (Union[Unset, GetApiV1ServerFollowersActorType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1ServerFollowersResponse200
     """


    return (await asyncio_detailed(
        client=client,
state=state,
actor_type=actor_type,
start=start,
count=count,
sort=sort,

    )).parsed
