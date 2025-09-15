from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_video_caption_body import AddVideoCaptionBody
from typing import cast
from typing import cast, Union
from uuid import UUID



def _get_kwargs(
    id: Union[UUID, int, str],
    caption_language: str,
    *,
    body: AddVideoCaptionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/videos/{id}/captions/{caption_language}".format(id=id,caption_language=caption_language,),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Union[UUID, int, str],
    caption_language: str,
    *,
    client: AuthenticatedClient,
    body: AddVideoCaptionBody,

) -> Response[Any]:
    """ Add or replace a video caption

    Args:
        id (Union[UUID, int, str]):
        caption_language (str): language id of the video (see
            [/videos/languages](#operation/getLanguages)) Example: en.
        body (AddVideoCaptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
caption_language=caption_language,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: Union[UUID, int, str],
    caption_language: str,
    *,
    client: AuthenticatedClient,
    body: AddVideoCaptionBody,

) -> Response[Any]:
    """ Add or replace a video caption

    Args:
        id (Union[UUID, int, str]):
        caption_language (str): language id of the video (see
            [/videos/languages](#operation/getLanguages)) Example: en.
        body (AddVideoCaptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
caption_language=caption_language,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

