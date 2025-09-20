from http import HTTPStatus
from typing import Any, cast

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.get_api_v1_plugins_npm_name_public_settings_response_200 import (
    GetApiV1PluginsNpmNamePublicSettingsResponse200,
)
from peertube.types import Response


def _get_kwargs(npm_name: str) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/plugins/{npm_name}/public-settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetApiV1PluginsNpmNamePublicSettingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiV1PluginsNpmNamePublicSettingsResponse200.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == 404:
        response_404 = cast("Any", None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetApiV1PluginsNpmNamePublicSettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    npm_name: str, *, client: AuthenticatedClient | Client
) -> Response[Any | GetApiV1PluginsNpmNamePublicSettingsResponse200]:
    """Get a plugin's public settings


    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1PluginsNpmNamePublicSettingsResponse200]]
    """

    kwargs = _get_kwargs(npm_name=npm_name)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    npm_name: str, *, client: AuthenticatedClient | Client
) -> Any | GetApiV1PluginsNpmNamePublicSettingsResponse200 | None:
    """Get a plugin's public settings


    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1PluginsNpmNamePublicSettingsResponse200]
    """

    return sync_detailed(npm_name=npm_name, client=client).parsed


async def asyncio_detailed(
    npm_name: str, *, client: AuthenticatedClient | Client
) -> Response[Any | GetApiV1PluginsNpmNamePublicSettingsResponse200]:
    """Get a plugin's public settings


    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiV1PluginsNpmNamePublicSettingsResponse200]]
    """

    kwargs = _get_kwargs(npm_name=npm_name)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    npm_name: str, *, client: AuthenticatedClient | Client
) -> Any | GetApiV1PluginsNpmNamePublicSettingsResponse200 | None:
    """Get a plugin's public settings


    Args:
        npm_name (str):  Example: peertube-plugin-auth-ldap.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiV1PluginsNpmNamePublicSettingsResponse200]
    """

    return (await asyncio_detailed(npm_name=npm_name, client=client)).parsed
