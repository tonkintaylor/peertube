from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_watched_words_accounts_account_name_lists_body import PostApiV1WatchedWordsAccountsAccountNameListsBody
from ...models.post_api_v1_watched_words_accounts_account_name_lists_response_200 import PostApiV1WatchedWordsAccountsAccountNameListsResponse200
from typing import cast



def _get_kwargs(
    account_name: str,
    *,
    body: PostApiV1WatchedWordsAccountsAccountNameListsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/watched-words/accounts/{account_name}/lists".format(account_name=account_name,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
    if response.status_code == 200:
        response_200 = PostApiV1WatchedWordsAccountsAccountNameListsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
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
    body: PostApiV1WatchedWordsAccountsAccountNameListsBody,

) -> Response[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
    """ Add account watched words

     **PeerTube >= 6.2**

    Args:
        account_name (str):
        body (PostApiV1WatchedWordsAccountsAccountNameListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]
     """


    kwargs = _get_kwargs(
        account_name=account_name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_name: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1WatchedWordsAccountsAccountNameListsBody,

) -> Optional[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
    """ Add account watched words

     **PeerTube >= 6.2**

    Args:
        account_name (str):
        body (PostApiV1WatchedWordsAccountsAccountNameListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1WatchedWordsAccountsAccountNameListsResponse200
     """


    return sync_detailed(
        account_name=account_name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1WatchedWordsAccountsAccountNameListsBody,

) -> Response[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
    """ Add account watched words

     **PeerTube >= 6.2**

    Args:
        account_name (str):
        body (PostApiV1WatchedWordsAccountsAccountNameListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]
     """


    kwargs = _get_kwargs(
        account_name=account_name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1WatchedWordsAccountsAccountNameListsBody,

) -> Optional[PostApiV1WatchedWordsAccountsAccountNameListsResponse200]:
    """ Add account watched words

     **PeerTube >= 6.2**

    Args:
        account_name (str):
        body (PostApiV1WatchedWordsAccountsAccountNameListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1WatchedWordsAccountsAccountNameListsResponse200
     """


    return (await asyncio_detailed(
        account_name=account_name,
client=client,
body=body,

    )).parsed
