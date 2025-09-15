from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_jobs_job_type import GetJobsJobType
from ...models.get_jobs_response_200 import GetJobsResponse200
from ...models.get_jobs_state import GetJobsState
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    state: GetJobsState,
    *,
    job_type: Union[Unset, GetJobsJobType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_job_type: Union[Unset, str] = UNSET
    if not isinstance(job_type, Unset):
        json_job_type = job_type.value

    params["jobType"] = json_job_type

    params["start"] = start

    params["count"] = count

    params["sort"] = sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/jobs/{state}".format(state=state,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetJobsResponse200]:
    if response.status_code == 200:
        response_200 = GetJobsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetJobsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    state: GetJobsState,
    *,
    client: AuthenticatedClient,
    job_type: Union[Unset, GetJobsJobType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[GetJobsResponse200]:
    """ List instance jobs

    Args:
        state (GetJobsState):
        job_type (Union[Unset, GetJobsJobType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobsResponse200]
     """


    kwargs = _get_kwargs(
        state=state,
job_type=job_type,
start=start,
count=count,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    state: GetJobsState,
    *,
    client: AuthenticatedClient,
    job_type: Union[Unset, GetJobsJobType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[GetJobsResponse200]:
    """ List instance jobs

    Args:
        state (GetJobsState):
        job_type (Union[Unset, GetJobsJobType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobsResponse200
     """


    return sync_detailed(
        state=state,
client=client,
job_type=job_type,
start=start,
count=count,
sort=sort,

    ).parsed

async def asyncio_detailed(
    state: GetJobsState,
    *,
    client: AuthenticatedClient,
    job_type: Union[Unset, GetJobsJobType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Response[GetJobsResponse200]:
    """ List instance jobs

    Args:
        state (GetJobsState):
        job_type (Union[Unset, GetJobsJobType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobsResponse200]
     """


    kwargs = _get_kwargs(
        state=state,
job_type=job_type,
start=start,
count=count,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    state: GetJobsState,
    *,
    client: AuthenticatedClient,
    job_type: Union[Unset, GetJobsJobType] = UNSET,
    start: Union[Unset, int] = UNSET,
    count: Union[Unset, int] = 15,
    sort: Union[Unset, str] = UNSET,

) -> Optional[GetJobsResponse200]:
    """ List instance jobs

    Args:
        state (GetJobsState):
        job_type (Union[Unset, GetJobsJobType]):
        start (Union[Unset, int]):
        count (Union[Unset, int]):  Default: 15.
        sort (Union[Unset, str]):  Example: -createdAt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobsResponse200
     """


    return (await asyncio_detailed(
        state=state,
client=client,
job_type=job_type,
start=start,
count=count,
sort=sort,

    )).parsed
