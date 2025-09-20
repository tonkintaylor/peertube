from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.put_api_v1_watched_words_accounts_account_name_lists_list_id_body import (
    PutApiV1WatchedWordsAccountsAccountNameListsListIdBody)
from peertube.types import Response


def _get_kwargs(
    account_name: str, list_id: str, *, body: PutApiV1WatchedWordsAccountsAccountNameListsListIdBody) -> dict[str, Any]:
    headers: dict[str, Any]={}

    _kwargs: dict[str, Any]={
        "method": "put", "url": f"/api/v1/watched-words/accounts/{account_name}/lists/{list_id}", }
    _kwargs["json"]=body.to_dict()

    headers["Content-Type"]="application/json"

    _kwargs["headers"]=headers
    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code== 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None

def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code = HTTPStatus(response.status_code), content = response.content, headers = response.headers, parsed = _parse_response(client=client, response=response))


def sync_detailed(
    account_name: str, list_id: str, *, client: AuthenticatedClient, body: PutApiV1WatchedWordsAccountsAccountNameListsListIdBody) -> Response[Any]:
    """Update account watched words

     **PeerTube >=6.2**
    Args:
        account_name (str): Parameter for account name.
        list_id (str): Parameter for list id.
        body (PutApiV1WatchedWordsAccountsAccountNameListsListIdBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_name=account_name, list_id=list_id, body=body)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client=client, response=response)


def sync(
    account_name: str, list_id: str, *, client: AuthenticatedClient, body: PutApiV1WatchedWordsAccountsAccountNameListsListIdBody) -> Any | None:
    """Update account watched words


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(
        account_name=account_name,
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_name: str, list_id: str, *, client: AuthenticatedClient, body: PutApiV1WatchedWordsAccountsAccountNameListsListIdBody) -> Response[Any]:
    """Update account watched words

     **PeerTube >=6.2**
    Args:
        account_name (str): Parameter for account name.
        list_id (str): Parameter for list id.
        body (PutApiV1WatchedWordsAccountsAccountNameListsListIdBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_name=account_name, list_id=list_id, body=body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

