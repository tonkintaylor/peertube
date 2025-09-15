from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.video_stats_user_agent_device import VideoStatsUserAgentDevice
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="VideoStatsUserAgentDevicesItem")



@_attrs_define
class VideoStatsUserAgentDevicesItem:
    """ 
        Attributes:
            name (Union[Unset, VideoStatsUserAgentDevice]):
            viewers (Union[Unset, float]):
     """

    name: Union[Unset, VideoStatsUserAgentDevice] = UNSET
    viewers: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value


        viewers = self.viewers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if viewers is not UNSET:
            field_dict["viewers"] = viewers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, VideoStatsUserAgentDevice]
        if isinstance(_name,  Unset):
            name = UNSET
        else:
            name = VideoStatsUserAgentDevice(_name)




        viewers = d.pop("viewers", UNSET)

        video_stats_user_agent_devices_item = cls(
            name=name,
            viewers=viewers,
        )


        video_stats_user_agent_devices_item.additional_properties = d
        return video_stats_user_agent_devices_item

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
