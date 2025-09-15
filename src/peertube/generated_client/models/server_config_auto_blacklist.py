from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_auto_blacklist_videos import ServerConfigAutoBlacklistVideos





T = TypeVar("T", bound="ServerConfigAutoBlacklist")



@_attrs_define
class ServerConfigAutoBlacklist:
    """ 
        Attributes:
            videos (Union[Unset, ServerConfigAutoBlacklistVideos]):
     """

    videos: Union[Unset, 'ServerConfigAutoBlacklistVideos'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_auto_blacklist_videos import ServerConfigAutoBlacklistVideos
        videos: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.videos, Unset):
            videos = self.videos.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_auto_blacklist_videos import ServerConfigAutoBlacklistVideos
        d = dict(src_dict)
        _videos = d.pop("videos", UNSET)
        videos: Union[Unset, ServerConfigAutoBlacklistVideos]
        if isinstance(_videos,  Unset):
            videos = UNSET
        else:
            videos = ServerConfigAutoBlacklistVideos.from_dict(_videos)




        server_config_auto_blacklist = cls(
            videos=videos,
        )


        server_config_auto_blacklist.additional_properties = d
        return server_config_auto_blacklist

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
