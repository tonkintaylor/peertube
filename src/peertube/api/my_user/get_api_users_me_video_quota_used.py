from http import HTTPStatus
from typing import Any

import httpx

from peertube import errors
from peertube.client import AuthenticatedClient, Client
from peertube.models.get_api_v1_users_me_video_quota_used_response_200 import (
    GetApiV1UsersMeVideoQuotaUsedResponse200,
)
from peertube.types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/me/video-quota-used",
    }

    return _kwargs

def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiV1UsersMeVideoQuotaUsedResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiV1UsersMeVideoQuotaUsedResponse200.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None

def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiV1UsersMeVideoQuotaUsedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetApiV1UsersMeVideoQuotaUsedResponse200]:
    """Get my user used quota

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1UsersMeVideoQuotaUsedResponse200]
    """
    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetApiV1UsersMeVideoQuotaUsedResponse200 | None:
    """Get my user used quota

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1UsersMeVideoQuotaUsedResponse200
    """
    return sync_detailed(
        client=client,
    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetApiV1UsersMeVideoQuotaUsedResponse200]:
    """Get my user used quota

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1UsersMeVideoQuotaUsedResponse200]
    """
    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetApiV1UsersMeVideoQuotaUsedResponse200 | None:
    """Get my user used quota

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1UsersMeVideoQuotaUsedResponse200
    """
    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
