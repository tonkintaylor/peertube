from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.verify_user_body import VerifyUserBody
from peertube.types import Response


def _get_kwargs(
    id: int,
    *,
    body: VerifyUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{id}/verify-email",
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

    if response.status_code == 403:
        return None

    if response.status_code == 404:
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyUserBody,
) -> Response[Any]:
    """Verify a user

     Following a user registration, the new user will receive an email asking to click a link
    containing a secret.
    This endpoint can also be used to verify a new email set in the user account.

    Args:
        id (int):  Example: 42.
        body (VerifyUserBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyUserBody,
) -> Response[Any]:
    """Verify a user

     Following a user registration, the new user will receive an email asking to click a link
    containing a secret.
    This endpoint can also be used to verify a new email set in the user account.

    Args:
        id (int):  Example: 42.
        body (VerifyUserBody): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
