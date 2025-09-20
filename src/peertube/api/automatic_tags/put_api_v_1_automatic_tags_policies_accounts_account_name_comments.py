from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.put_api_v1_automatic_tags_policies_accounts_account_name_comments_body import (
    PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody,
)
from peertube.types import Response


def _get_kwargs(
    account_name: str,
    *,
    body: PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/automatic-tags/policies/accounts/{account_name}/comments",
    }
    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
    body: PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody,
) -> Response[Any]:
    """Update account auto tag policies on comments

     **PeerTube > = 6.2**
    Args:
        account_name (str): Parameter for account name.
        body (PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(account_name=account_name, body=body)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    account_name: str,
    *,
    client: AuthenticatedClient,
    body: PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody,
) -> Any | None:
    """Update account auto tag policies on comments


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(account_name=account_name, client=client, body=body).parsed


async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,
    body: PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody,
) -> Response[Any]:
    """Update account auto tag policies on comments

     **PeerTube > = 6.2**
    Args:
        account_name (str): Parameter for account name.
        body (PutApiV1AutomaticTagsPoliciesAccountsAccountNameCommentsBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(account_name=account_name, body=body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
