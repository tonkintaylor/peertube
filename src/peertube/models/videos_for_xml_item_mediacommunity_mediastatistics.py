from collections.abc import Mapping
from typing import (
    Any, TypeVar)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.types import UNSET, Unset

T=TypeVar("T", bound="VideosForXMLItemMediacommunityMediastatistics")


@_attrs_define
class VideosForXMLItemMediacommunityMediastatistics:
    """Attributes:
    views (Union[Unset, int]):
    """


    views: Unset | int = UNSET
    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""

        views=self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if views is not UNSET:
            field_dict["views"]=views

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""

        d = dict(src_dict)
        views=d.pop("views", UNSET)

        videos_for_xml_item_mediacommunity_mediastatistics=cls(
            views=views)

        videos_for_xml_item_mediacommunity_mediastatistics.additional_properties=d
        return videos_for_xml_item_mediacommunity_mediastatistics

    @property
    def additional_keys(self) -> list[str]:
        """Get additional property keys."""

        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

