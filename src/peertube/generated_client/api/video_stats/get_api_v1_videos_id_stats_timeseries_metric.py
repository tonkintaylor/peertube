from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_v1_videos_id_stats_timeseries_metric_metric import GetApiV1VideosIdStatsTimeseriesMetricMetric
from ...models.video_stats_timeserie import VideoStatsTimeserie
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID
import datetime



def _get_kwargs(
    id: Union[UUID, int, str],
    metric: GetApiV1VideosIdStatsTimeseriesMetricMetric,
    *,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/videos/{id}/stats/timeseries/{metric}".format(id=id,metric=metric,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VideoStatsTimeserie]:
    if response.status_code == 200:
        response_200 = VideoStatsTimeserie.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VideoStatsTimeserie]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Union[UUID, int, str],
    metric: GetApiV1VideosIdStatsTimeseriesMetricMetric,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,

) -> Response[VideoStatsTimeserie]:
    """ Get timeserie stats of a video

    Args:
        id (Union[UUID, int, str]):
        metric (GetApiV1VideosIdStatsTimeseriesMetricMetric):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoStatsTimeserie]
     """


    kwargs = _get_kwargs(
        id=id,
metric=metric,
start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: Union[UUID, int, str],
    metric: GetApiV1VideosIdStatsTimeseriesMetricMetric,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,

) -> Optional[VideoStatsTimeserie]:
    """ Get timeserie stats of a video

    Args:
        id (Union[UUID, int, str]):
        metric (GetApiV1VideosIdStatsTimeseriesMetricMetric):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoStatsTimeserie
     """


    return sync_detailed(
        id=id,
metric=metric,
client=client,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    id: Union[UUID, int, str],
    metric: GetApiV1VideosIdStatsTimeseriesMetricMetric,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,

) -> Response[VideoStatsTimeserie]:
    """ Get timeserie stats of a video

    Args:
        id (Union[UUID, int, str]):
        metric (GetApiV1VideosIdStatsTimeseriesMetricMetric):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoStatsTimeserie]
     """


    kwargs = _get_kwargs(
        id=id,
metric=metric,
start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: Union[UUID, int, str],
    metric: GetApiV1VideosIdStatsTimeseriesMetricMetric,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,

) -> Optional[VideoStatsTimeserie]:
    """ Get timeserie stats of a video

    Args:
        id (Union[UUID, int, str]):
        metric (GetApiV1VideosIdStatsTimeseriesMetricMetric):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoStatsTimeserie
     """


    return (await asyncio_detailed(
        id=id,
metric=metric,
client=client,
start_date=start_date,
end_date=end_date,

    )).parsed
