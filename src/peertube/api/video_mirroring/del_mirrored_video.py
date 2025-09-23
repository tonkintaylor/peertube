from typing import Any

import httpx
from pydantic import ConfigDict, validate_call

from peertube import errors
from peertube.api.shared_utils import build_response
from peertube.client import AuthenticatedClient, Client
from peertube.types import Response


def _get_kwargs(redundancy_id: str) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/server/redundancy/videos/{redundancy_id}",
    }

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
    return build_response(client=client, response=response)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def sync_detailed(redundancy_id: str, *, client: AuthenticatedClient) -> Response[Any]:
    """Delete a mirror done on a video


    Args:
        redundancy_id (str): Parameter for redundancy id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(redundancy_id=redundancy_id)

    response = client.get_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def sync(redundancy_id: str, *, client: AuthenticatedClient) -> Any | None:
    """Delete a mirror done on a video


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any
    """

    return sync_detailed(redundancy_id=redundancy_id, client=client).parsed


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
async def asyncio_detailed(
    redundancy_id: str, *, client: AuthenticatedClient
) -> Response[Any]:
    """Delete a mirror done on a video


    Args:
        redundancy_id (str): Parameter for redundancy id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(redundancy_id=redundancy_id)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
