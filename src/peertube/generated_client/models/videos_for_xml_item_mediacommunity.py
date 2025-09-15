from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.videos_for_xml_item_mediacommunity_mediastatistics import VideosForXMLItemMediacommunityMediastatistics





T = TypeVar("T", bound="VideosForXMLItemMediacommunity")



@_attrs_define
class VideosForXMLItemMediacommunity:
    """ see [media:community](https://www.rssboard.org/media-rss#media-community) (MRSS)

        Attributes:
            mediastatistics (Union[Unset, VideosForXMLItemMediacommunityMediastatistics]):
     """

    mediastatistics: Union[Unset, 'VideosForXMLItemMediacommunityMediastatistics'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.videos_for_xml_item_mediacommunity_mediastatistics import VideosForXMLItemMediacommunityMediastatistics
        mediastatistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mediastatistics, Unset):
            mediastatistics = self.mediastatistics.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mediastatistics is not UNSET:
            field_dict["media:statistics"] = mediastatistics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.videos_for_xml_item_mediacommunity_mediastatistics import VideosForXMLItemMediacommunityMediastatistics
        d = dict(src_dict)
        _mediastatistics = d.pop("media:statistics", UNSET)
        mediastatistics: Union[Unset, VideosForXMLItemMediacommunityMediastatistics]
        if isinstance(_mediastatistics,  Unset):
            mediastatistics = UNSET
        else:
            mediastatistics = VideosForXMLItemMediacommunityMediastatistics.from_dict(_mediastatistics)




        videos_for_xml_item_mediacommunity = cls(
            mediastatistics=mediastatistics,
        )


        videos_for_xml_item_mediacommunity.additional_properties = d
        return videos_for_xml_item_mediacommunity

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
