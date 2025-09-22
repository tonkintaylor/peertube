from typing import Any, Union

import httpx

from peertube import errors
from peertube.api.shared_utils import build_response
from peertube.client import AuthenticatedClient, Client
from peertube.models.update_plugin_body_type_0 import UpdatePluginBodyType0
from peertube.models.update_plugin_body_type_1 import UpdatePluginBodyType1
from peertube.types import Response


def _get_kwargs(
    *, body: Union["UpdatePluginBodyType0", "UpdatePluginBodyType1"]
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/plugins/update",
    }
    if isinstance(body, UpdatePluginBodyType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
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
    return build_response(client=client, response=response)


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["UpdatePluginBodyType0", "UpdatePluginBodyType1"],
) -> Response[Any]:
    """Update a plugin


    Args:
        body (Union['UpdatePluginBodyType0', 'UpdatePluginBodyType1']): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(body=body)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union["UpdatePluginBodyType0", "UpdatePluginBodyType1"],
) -> Any | None:
    """Update a plugin


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(client=client, body=body).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["UpdatePluginBodyType0", "UpdatePluginBodyType1"],
) -> Response[Any]:
    """Update a plugin


    Args:
        body (Union['UpdatePluginBodyType0', 'UpdatePluginBodyType1']): Request body data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(body=body)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
