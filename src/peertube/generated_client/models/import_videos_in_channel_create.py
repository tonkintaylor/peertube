from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ImportVideosInChannelCreate")



@_attrs_define
class ImportVideosInChannelCreate:
    """ 
        Attributes:
            external_channel_url (str):  Example: https://youtube.com/c/UC_myfancychannel.
            video_channel_sync_id (Union[Unset, int]): If part of a channel sync process, specify its id to assign video
                imports to this channel synchronization
     """

    external_channel_url: str
    video_channel_sync_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_channel_url = self.external_channel_url

        video_channel_sync_id = self.video_channel_sync_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "externalChannelUrl": external_channel_url,
        })
        if video_channel_sync_id is not UNSET:
            field_dict["videoChannelSyncId"] = video_channel_sync_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_channel_url = d.pop("externalChannelUrl")

        video_channel_sync_id = d.pop("videoChannelSyncId", UNSET)

        import_videos_in_channel_create = cls(
            external_channel_url=external_channel_url,
            video_channel_sync_id=video_channel_sync_id,
        )


        import_videos_in_channel_create.additional_properties = d
        return import_videos_in_channel_create

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
