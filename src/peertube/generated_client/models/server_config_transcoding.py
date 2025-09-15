from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_transcoding_web_videos import ServerConfigTranscodingWebVideos
  from ..models.server_config_transcoding_hls import ServerConfigTranscodingHls





T = TypeVar("T", bound="ServerConfigTranscoding")



@_attrs_define
class ServerConfigTranscoding:
    """ 
        Attributes:
            hls (Union[Unset, ServerConfigTranscodingHls]):
            web_videos (Union[Unset, ServerConfigTranscodingWebVideos]):
            enabled_resolutions (Union[Unset, list[int]]):
     """

    hls: Union[Unset, 'ServerConfigTranscodingHls'] = UNSET
    web_videos: Union[Unset, 'ServerConfigTranscodingWebVideos'] = UNSET
    enabled_resolutions: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_transcoding_web_videos import ServerConfigTranscodingWebVideos
        from ..models.server_config_transcoding_hls import ServerConfigTranscodingHls
        hls: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hls, Unset):
            hls = self.hls.to_dict()

        web_videos: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.web_videos, Unset):
            web_videos = self.web_videos.to_dict()

        enabled_resolutions: Union[Unset, list[int]] = UNSET
        if not isinstance(self.enabled_resolutions, Unset):
            enabled_resolutions = self.enabled_resolutions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hls is not UNSET:
            field_dict["hls"] = hls
        if web_videos is not UNSET:
            field_dict["web_videos"] = web_videos
        if enabled_resolutions is not UNSET:
            field_dict["enabledResolutions"] = enabled_resolutions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_transcoding_web_videos import ServerConfigTranscodingWebVideos
        from ..models.server_config_transcoding_hls import ServerConfigTranscodingHls
        d = dict(src_dict)
        _hls = d.pop("hls", UNSET)
        hls: Union[Unset, ServerConfigTranscodingHls]
        if isinstance(_hls,  Unset):
            hls = UNSET
        else:
            hls = ServerConfigTranscodingHls.from_dict(_hls)




        _web_videos = d.pop("web_videos", UNSET)
        web_videos: Union[Unset, ServerConfigTranscodingWebVideos]
        if isinstance(_web_videos,  Unset):
            web_videos = UNSET
        else:
            web_videos = ServerConfigTranscodingWebVideos.from_dict(_web_videos)




        enabled_resolutions = cast(list[int], d.pop("enabledResolutions", UNSET))


        server_config_transcoding = cls(
            hls=hls,
            web_videos=web_videos,
            enabled_resolutions=enabled_resolutions,
        )


        server_config_transcoding.additional_properties = d
        return server_config_transcoding

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
