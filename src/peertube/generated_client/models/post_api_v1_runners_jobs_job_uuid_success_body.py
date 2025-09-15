from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.vod_audio_merge_transcoding import VODAudioMergeTranscoding
  from ..models.vod_web_video_transcoding import VODWebVideoTranscoding
  from ..models.live_rtmp_to_hls_transcoding import LiveRTMPToHLSTranscoding
  from ..models.vodhls_transcoding import VODHLSTranscoding





T = TypeVar("T", bound="PostApiV1RunnersJobsJobUUIDSuccessBody")



@_attrs_define
class PostApiV1RunnersJobsJobUUIDSuccessBody:
    """ 
        Attributes:
            runner_token (str):
            job_token (str):
            payload (Union['LiveRTMPToHLSTranscoding', 'VODAudioMergeTranscoding', 'VODHLSTranscoding',
                'VODWebVideoTranscoding']):
     """

    runner_token: str
    job_token: str
    payload: Union['LiveRTMPToHLSTranscoding', 'VODAudioMergeTranscoding', 'VODHLSTranscoding', 'VODWebVideoTranscoding']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vod_audio_merge_transcoding import VODAudioMergeTranscoding
        from ..models.vod_web_video_transcoding import VODWebVideoTranscoding
        from ..models.live_rtmp_to_hls_transcoding import LiveRTMPToHLSTranscoding
        from ..models.vodhls_transcoding import VODHLSTranscoding
        runner_token = self.runner_token

        job_token = self.job_token

        payload: dict[str, Any]
        if isinstance(self.payload, VODWebVideoTranscoding):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, VODHLSTranscoding):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, VODAudioMergeTranscoding):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runnerToken": runner_token,
            "jobToken": job_token,
            "payload": payload,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vod_audio_merge_transcoding import VODAudioMergeTranscoding
        from ..models.vod_web_video_transcoding import VODWebVideoTranscoding
        from ..models.live_rtmp_to_hls_transcoding import LiveRTMPToHLSTranscoding
        from ..models.vodhls_transcoding import VODHLSTranscoding
        d = dict(src_dict)
        runner_token = d.pop("runnerToken")

        job_token = d.pop("jobToken")

        def _parse_payload(data: object) -> Union['LiveRTMPToHLSTranscoding', 'VODAudioMergeTranscoding', 'VODHLSTranscoding', 'VODWebVideoTranscoding']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_vod_web_video_transcoding = VODWebVideoTranscoding.from_dict(data)



                return payload_vod_web_video_transcoding
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_vod_hls_transcoding = VODHLSTranscoding.from_dict(data)



                return payload_vod_hls_transcoding
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_vod_audio_merge_transcoding = VODAudioMergeTranscoding.from_dict(data)



                return payload_vod_audio_merge_transcoding
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payload_live_rtmp_to_hls_transcoding = LiveRTMPToHLSTranscoding.from_dict(data)



            return payload_live_rtmp_to_hls_transcoding

        payload = _parse_payload(d.pop("payload"))


        post_api_v1_runners_jobs_job_uuid_success_body = cls(
            runner_token=runner_token,
            job_token=job_token,
            payload=payload,
        )


        post_api_v1_runners_jobs_job_uuid_success_body.additional_properties = d
        return post_api_v1_runners_jobs_job_uuid_success_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
