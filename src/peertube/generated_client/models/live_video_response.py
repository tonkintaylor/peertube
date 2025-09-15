from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.live_video_latency_mode import LiveVideoLatencyMode
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.live_video_replay_settings import LiveVideoReplaySettings
  from ..models.live_schedule import LiveSchedule





T = TypeVar("T", bound="LiveVideoResponse")



@_attrs_define
class LiveVideoResponse:
    """ 
        Attributes:
            rtmp_url (Union[Unset, str]): Included in the response if an appropriate token is provided
            rtmps_url (Union[Unset, str]): Included in the response if an appropriate token is provided
            stream_key (Union[Unset, str]): RTMP stream key to use to stream into this live video. Included in the response
                if an appropriate token is provided
            save_replay (Union[Unset, bool]):
            replay_settings (Union[Unset, LiveVideoReplaySettings]):
            permanent_live (Union[Unset, bool]): User can stream multiple times in a permanent live
            latency_mode (Union[Unset, LiveVideoLatencyMode]): The live latency mode (Default = `1`, High latency = `2`,
                Small Latency = `3`)
            schedules (Union[Unset, list['LiveSchedule']]):
     """

    rtmp_url: Union[Unset, str] = UNSET
    rtmps_url: Union[Unset, str] = UNSET
    stream_key: Union[Unset, str] = UNSET
    save_replay: Union[Unset, bool] = UNSET
    replay_settings: Union[Unset, 'LiveVideoReplaySettings'] = UNSET
    permanent_live: Union[Unset, bool] = UNSET
    latency_mode: Union[Unset, LiveVideoLatencyMode] = UNSET
    schedules: Union[Unset, list['LiveSchedule']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.live_video_replay_settings import LiveVideoReplaySettings
        from ..models.live_schedule import LiveSchedule
        rtmp_url = self.rtmp_url

        rtmps_url = self.rtmps_url

        stream_key = self.stream_key

        save_replay = self.save_replay

        replay_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.replay_settings, Unset):
            replay_settings = self.replay_settings.to_dict()

        permanent_live = self.permanent_live

        latency_mode: Union[Unset, int] = UNSET
        if not isinstance(self.latency_mode, Unset):
            latency_mode = self.latency_mode.value


        schedules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()
                schedules.append(schedules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rtmp_url is not UNSET:
            field_dict["rtmpUrl"] = rtmp_url
        if rtmps_url is not UNSET:
            field_dict["rtmpsUrl"] = rtmps_url
        if stream_key is not UNSET:
            field_dict["streamKey"] = stream_key
        if save_replay is not UNSET:
            field_dict["saveReplay"] = save_replay
        if replay_settings is not UNSET:
            field_dict["replaySettings"] = replay_settings
        if permanent_live is not UNSET:
            field_dict["permanentLive"] = permanent_live
        if latency_mode is not UNSET:
            field_dict["latencyMode"] = latency_mode
        if schedules is not UNSET:
            field_dict["schedules"] = schedules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_video_replay_settings import LiveVideoReplaySettings
        from ..models.live_schedule import LiveSchedule
        d = dict(src_dict)
        rtmp_url = d.pop("rtmpUrl", UNSET)

        rtmps_url = d.pop("rtmpsUrl", UNSET)

        stream_key = d.pop("streamKey", UNSET)

        save_replay = d.pop("saveReplay", UNSET)

        _replay_settings = d.pop("replaySettings", UNSET)
        replay_settings: Union[Unset, LiveVideoReplaySettings]
        if isinstance(_replay_settings,  Unset):
            replay_settings = UNSET
        else:
            replay_settings = LiveVideoReplaySettings.from_dict(_replay_settings)




        permanent_live = d.pop("permanentLive", UNSET)

        _latency_mode = d.pop("latencyMode", UNSET)
        latency_mode: Union[Unset, LiveVideoLatencyMode]
        if isinstance(_latency_mode,  Unset):
            latency_mode = UNSET
        else:
            latency_mode = LiveVideoLatencyMode(_latency_mode)




        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in (_schedules or []):
            schedules_item = LiveSchedule.from_dict(schedules_item_data)



            schedules.append(schedules_item)


        live_video_response = cls(
            rtmp_url=rtmp_url,
            rtmps_url=rtmps_url,
            stream_key=stream_key,
            save_replay=save_replay,
            replay_settings=replay_settings,
            permanent_live=permanent_live,
            latency_mode=latency_mode,
            schedules=schedules,
        )


        live_video_response.additional_properties = d
        return live_video_response

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
