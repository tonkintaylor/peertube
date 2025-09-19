from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.server_config_about import ServerConfigAbout
from peertube.types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any]={
        "method": "get", "url": "/api/v1/config/about", }

    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerConfigAbout | None:
    if response.status_code== 200:
        response_200 = ServerConfigAbout.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None

def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServerConfigAbout]:
    return Response(
        status_code = HTTPStatus(response.status_code), content = response.content, headers = response.headers, parsed = _parse_response(client = client, response = response))



def sync_detailed(
    *, client: AuthenticatedClient | Client) -> Response[ServerConfigAbout]:
    r"""Get instance \"About\" information


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerConfigAbout]
    """
    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs)

    return _build_response(client = client, response = response)



def sync(
    *, client: AuthenticatedClient | Client) -> ServerConfigAbout | None:
    r"""Get instance \"About\" information


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerConfigAbout
    """
    return sync_detailed(
        client = client).parsed


async def asyncio_detailed(
    *, client: AuthenticatedClient | Client) -> Response[ServerConfigAbout]:
    r"""Get instance \"About\" information


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerConfigAbout]
    """
    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client = client, response = response)



async def asyncio(
    *, client: AuthenticatedClient | Client) -> ServerConfigAbout | None:
    r"""Get instance \"About\" information


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerConfigAbout
    """
    return (
        await asyncio_detailed(
            client = client)
    ).parsed
