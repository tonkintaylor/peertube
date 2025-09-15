from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notification_type import NotificationType
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    type_one_of: Union[Unset, list[NotificationType]] = UNSET,
    unread: Union[Unset, bool] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_one_of: Union[Unset, list[int]] = UNSET
    if not isinstance(type_one_of, Unset):
        json_type_one_of = []
        for type_one_of_item_data in type_one_of:
            type_one_of_item = type_one_of_item_data.value
            json_type_one_of.append(type_one_of_item)


    params["typeOneOf"] = json_type_one_of

    params["unread"] = unread

    params["start"] = start

    params["count"] = count

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/notifications",
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
    type_one_of: Union[Unset, list[NotificationType]] = UNSET,
    unread: Union[Unset, bool] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ List my notifications

    Args:
        type_one_of (Union[Unset, list[NotificationType]]):
        unread (Union[Unset, bool]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        type_one_of=type_one_of,
unread=unread,
start=start,
count=count,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_one_of: Union[Unset, list[NotificationType]] = UNSET,
    unread: Union[Unset, bool] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ List my notifications

    Args:
        type_one_of (Union[Unset, list[NotificationType]]):
        unread (Union[Unset, bool]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        type_one_of=type_one_of,
unread=unread,
start=start,
count=count,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

