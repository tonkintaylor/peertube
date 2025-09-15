from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="VideoStreamingPlaylistsHLSRedundanciesItem")



@_attrs_define
class VideoStreamingPlaylistsHLSRedundanciesItem:
    """ 
        Attributes:
            base_url (Union[Unset, str]):
     """

    base_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        video_streaming_playlists_hls_redundancies_item = cls(
            base_url=base_url,
        )


        video_streaming_playlists_hls_redundancies_item.additional_properties = d
        return video_streaming_playlists_hls_redundancies_item

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
