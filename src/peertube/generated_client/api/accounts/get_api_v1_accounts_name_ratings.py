from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_v1_accounts_name_ratings_rating import GetApiV1AccountsNameRatingsRating
from ...models.video_rating import VideoRating
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    name: str,
    *,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    rating: Union[Unset, GetApiV1AccountsNameRatingsRating] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["count"] = count

    params["sort"] = sort

    json_rating: Union[Unset, str] = UNSET
    if not isinstance(rating, Unset):
        json_rating = rating.value

    params["rating"] = json_rating


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{name}/ratings".format(name=name,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['VideoRating']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = VideoRating.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['VideoRating']]:
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
    sort: Union[Unset, str] = UNSET,
    rating: Union[Unset, GetApiV1AccountsNameRatingsRating] = UNSET,

) -> Response[list['VideoRating']]:
    """ List ratings of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        rating (Union[Unset, GetApiV1AccountsNameRatingsRating]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VideoRating']]
     """


    kwargs = _get_kwargs(
        name=name,
start=start,
count=count,
sort=sort,
rating=rating,

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
    sort: Union[Unset, str] = UNSET,
    rating: Union[Unset, GetApiV1AccountsNameRatingsRating] = UNSET,

) -> Optional[list['VideoRating']]:
    """ List ratings of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        rating (Union[Unset, GetApiV1AccountsNameRatingsRating]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VideoRating']
     """


    return sync_detailed(
        name=name,
client=client,
start=start,
count=count,
sort=sort,
rating=rating,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,
    rating: Union[Unset, GetApiV1AccountsNameRatingsRating] = UNSET,

) -> Response[list['VideoRating']]:
    """ List ratings of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        rating (Union[Unset, GetApiV1AccountsNameRatingsRating]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VideoRating']]
     """


    kwargs = _get_kwargs(
        name=name,
start=start,
count=count,
sort=sort,
rating=rating,

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
    sort: Union[Unset, str] = UNSET,
    rating: Union[Unset, GetApiV1AccountsNameRatingsRating] = UNSET,

) -> Optional[list['VideoRating']]:
    """ List ratings of an account

    Args:
        name (str):  Example: chocobozzz | chocobozzz@example.org.
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.
        rating (Union[Unset, GetApiV1AccountsNameRatingsRating]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VideoRating']
     """


    return (await asyncio_detailed(
        name=name,
client=client,
start=start,
count=count,
sort=sort,
rating=rating,

    )).parsed
