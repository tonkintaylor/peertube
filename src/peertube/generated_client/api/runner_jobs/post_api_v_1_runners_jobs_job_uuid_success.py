from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_runners_jobs_job_uuid_success_body import PostApiV1RunnersJobsJobUUIDSuccessBody
from typing import cast
from uuid import UUID



def _get_kwargs(
    job_uuid: UUID,
    *,
    body: PostApiV1RunnersJobsJobUUIDSuccessBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runners/jobs/{job_uuid}/success".format(job_uuid=job_uuid,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
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
    job_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiV1RunnersJobsJobUUIDSuccessBody,

) -> Response[Any]:
    """ Post job success

     API used by PeerTube runners

    Args:
        job_uuid (UUID):  Example: 9c9de5e8-0a1e-484a-b099-e80766180a6d.
        body (PostApiV1RunnersJobsJobUUIDSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        job_uuid=job_uuid,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    job_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiV1RunnersJobsJobUUIDSuccessBody,

) -> Response[Any]:
    """ Post job success

     API used by PeerTube runners

    Args:
        job_uuid (UUID):  Example: 9c9de5e8-0a1e-484a-b099-e80766180a6d.
        body (PostApiV1RunnersJobsJobUUIDSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        job_uuid=job_uuid,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

