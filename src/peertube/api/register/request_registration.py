from http import HTTPStatus
from typing import Any, cast

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.user_registration import UserRegistration
from peertube.models.user_registration_request import UserRegistrationRequest
from peertube.types import Response


def _get_kwargs(
    *, body: UserRegistrationRequest) -> dict[str, Any]:
    headers: dict[str, Any]={}

    _kwargs: dict[str, Any]={
        "method": "post", "url": "/api/v1/users/registrations/request", }
    _kwargs["json"]=body.to_dict()

    headers["Content-Type"]="application/json"

    _kwargs["headers"]=headers
    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UserRegistration | None:
    if response.status_code== 200:
        response_200 = UserRegistration.from_dict(response.json())

        return response_200
    if response.status_code== 400:
        response_400 = cast("Any", None)
        return response_400
    if response.status_code== 403:
        response_403 = cast("Any", None)
        return response_403
    if response.status_code== 409:
        response_409 = cast("Any", None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None

def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UserRegistration]:
    return Response(
        status_code = HTTPStatus(response.status_code), content = response.content, headers = response.headers, parsed = _parse_response(client = client, response = response))


def sync_detailed(
    *, client: AuthenticatedClient | Client, body: UserRegistrationRequest) -> Response[Any | UserRegistration]:
    """Request registration

     Signup has to be enabled and require approval on the instance
    Args:
        client: Authenticated HTTP client for API requests.
        body (UserRegistrationRequest): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
    Returns:
        Response[Union[Any, UserRegistration]]
    """

    kwargs = _get_kwargs(
        body = body)

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)


def sync(
    *, client: AuthenticatedClient | Client, body: UserRegistrationRequest) -> Any | UserRegistration | None:
    """Request registration

     Signup has to be enabled and require approval on the instance
    Args:
        client: Authenticated HTTP client for API requests.
        body (UserRegistrationRequest): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
    Returns:
        Union[Any, UserRegistration]
    """

    return sync_detailed(
        client = client, body = body).parsed


async def asyncio_detailed(
    *, client: AuthenticatedClient | Client, body: UserRegistrationRequest) -> Response[Any | UserRegistration]:
    """Request registration

     Signup has to be enabled and require approval on the instance
    Args:
        client: Authenticated HTTP client for API requests.
        body (UserRegistrationRequest): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
    Returns:
        Response[Union[Any, UserRegistration]]
    """

    kwargs = _get_kwargs(
        body = body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)


async def asyncio(
    *, client: AuthenticatedClient | Client, body: UserRegistrationRequest) -> Any | UserRegistration | None:
    """Request registration

     Signup has to be enabled and require approval on the instance
    Args:
        client: Authenticated HTTP client for API requests.
        body (UserRegistrationRequest): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.
    Returns:
        Union[Any, UserRegistration]
    """

    return (
        await asyncio_detailed(
            client = client, body = body)
    ).parsed
