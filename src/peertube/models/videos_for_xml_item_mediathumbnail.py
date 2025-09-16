from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.types import UNSET, Unset

T = TypeVar("T", bound="VideosForXMLItemMediathumbnail")


@_attrs_define
class VideosForXMLItemMediathumbnail:
    """Attributes:
    url (Union[Unset, str]):
    height (Union[Unset, int]):
    width (Union[Unset, int]):
    """

    url: Unset | str = UNSET
    height: Unset | int = UNSET
    width: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""
        url = self.url

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        videos_for_xml_item_mediathumbnail = cls(
            url=url,
            height=height,
            width=width,
        )

        videos_for_xml_item_mediathumbnail.additional_properties = d
        return videos_for_xml_item_mediathumbnail

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
