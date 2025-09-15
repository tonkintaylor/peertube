from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_syndicated_comments_format import GetSyndicatedCommentsFormat
from ...models.video_comments_for_xml_item import VideoCommentsForXMLItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    format_: GetSyndicatedCommentsFormat,
    *,
    video_id: Unset | str = UNSET,
    account_id: Unset | str = UNSET,
    account_name: Unset | str = UNSET,
    video_channel_id: Unset | str = UNSET,
    video_channel_name: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["videoId"] = video_id

    params["accountId"] = account_id

    params["accountName"] = account_name

    params["videoChannelId"] = video_channel_id

    params["videoChannelName"] = video_channel_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/feeds/video-comments.{format_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list["VideoCommentsForXMLItem"] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for componentsschemas_video_comments_for_xml_item_data in _response_200:
            componentsschemas_video_comments_for_xml_item = (
                VideoCommentsForXMLItem.from_dict(
                    componentsschemas_video_comments_for_xml_item_data
                )
            )

            response_200.append(componentsschemas_video_comments_for_xml_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast("Any", None)
        return response_400

    if response.status_code == 404:
        response_404 = cast("Any", None)
        return response_404

    if response.status_code == 406:
        response_406 = cast("Any", None)
        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list["VideoCommentsForXMLItem"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    format_: GetSyndicatedCommentsFormat,
    *,
    client: AuthenticatedClient | Client,
    video_id: Unset | str = UNSET,
    account_id: Unset | str = UNSET,
    account_name: Unset | str = UNSET,
    video_channel_id: Unset | str = UNSET,
    video_channel_name: Unset | str = UNSET,
) -> Response[Any | list["VideoCommentsForXMLItem"]]:
    """Comments on videos feeds

    Args:
        format_ (GetSyndicatedCommentsFormat):
        video_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        account_name (Union[Unset, str]):
        video_channel_id (Union[Unset, str]):
        video_channel_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['VideoCommentsForXMLItem']]]
    """

    kwargs = _get_kwargs(
        format_=format_,
        video_id=video_id,
        account_id=account_id,
        account_name=account_name,
        video_channel_id=video_channel_id,
        video_channel_name=video_channel_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    format_: GetSyndicatedCommentsFormat,
    *,
    client: AuthenticatedClient | Client,
    video_id: Unset | str = UNSET,
    account_id: Unset | str = UNSET,
    account_name: Unset | str = UNSET,
    video_channel_id: Unset | str = UNSET,
    video_channel_name: Unset | str = UNSET,
) -> Any | list["VideoCommentsForXMLItem"] | None:
    """Comments on videos feeds

    Args:
        format_ (GetSyndicatedCommentsFormat):
        video_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        account_name (Union[Unset, str]):
        video_channel_id (Union[Unset, str]):
        video_channel_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['VideoCommentsForXMLItem']]
    """

    return sync_detailed(
        format_=format_,
        client=client,
        video_id=video_id,
        account_id=account_id,
        account_name=account_name,
        video_channel_id=video_channel_id,
        video_channel_name=video_channel_name,
    ).parsed


async def asyncio_detailed(
    format_: GetSyndicatedCommentsFormat,
    *,
    client: AuthenticatedClient | Client,
    video_id: Unset | str = UNSET,
    account_id: Unset | str = UNSET,
    account_name: Unset | str = UNSET,
    video_channel_id: Unset | str = UNSET,
    video_channel_name: Unset | str = UNSET,
) -> Response[Any | list["VideoCommentsForXMLItem"]]:
    """Comments on videos feeds

    Args:
        format_ (GetSyndicatedCommentsFormat):
        video_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        account_name (Union[Unset, str]):
        video_channel_id (Union[Unset, str]):
        video_channel_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['VideoCommentsForXMLItem']]]
    """

    kwargs = _get_kwargs(
        format_=format_,
        video_id=video_id,
        account_id=account_id,
        account_name=account_name,
        video_channel_id=video_channel_id,
        video_channel_name=video_channel_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    format_: GetSyndicatedCommentsFormat,
    *,
    client: AuthenticatedClient | Client,
    video_id: Unset | str = UNSET,
    account_id: Unset | str = UNSET,
    account_name: Unset | str = UNSET,
    video_channel_id: Unset | str = UNSET,
    video_channel_name: Unset | str = UNSET,
) -> Any | list["VideoCommentsForXMLItem"] | None:
    """Comments on videos feeds

    Args:
        format_ (GetSyndicatedCommentsFormat):
        video_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        account_name (Union[Unset, str]):
        video_channel_id (Union[Unset, str]):
        video_channel_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['VideoCommentsForXMLItem']]
    """

    return (
        await asyncio_detailed(
            format_=format_,
            client=client,
            video_id=video_id,
            account_id=account_id,
            account_name=account_name,
            video_channel_id=video_channel_id,
            video_channel_name=video_channel_name,
        )
    ).parsed
