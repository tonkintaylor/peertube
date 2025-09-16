from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.put_api_v1_plugins_npm_name_settings_body import (
    PutApiV1PluginsNpmNameSettingsBody,
)
from peertube.types import Response


def _get_kwargs(
    npm_name: str,
    *,
    body: PutApiV1PluginsNpmNameSettingsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/plugins/{npm_name}/settings",
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
    npm_name: str,
    *,
    client: AuthenticatedClient,
    body: PutApiV1PluginsNpmNameSettingsBody,
) -> Response[Any]:
    """Set a plugin's settings

    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.
        body (PutApiV1PluginsNpmNameSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        npm_name=npm_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    npm_name: str,
    *,
    client: AuthenticatedClient,
    body: PutApiV1PluginsNpmNameSettingsBody,
) -> Response[Any]:
    """Set a plugin's settings

    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.
        body (PutApiV1PluginsNpmNameSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        npm_name=npm_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
