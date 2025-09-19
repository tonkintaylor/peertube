from collections.abc import Mapping
from typing import (
    Any, TypeVar)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.types import UNSET, Unset

T=TypeVar("T", bound="VideoConstantStringLanguage")


@_attrs_define
class VideoConstantStringLanguage:
    """Attributes:
    id (Union[Unset, str]): language id of the video (see [/videos/languages](#operation/getLanguages)) Example: en.
    label (Union[Unset, str]):  Example: English.
    """


    id: Unset | str=UNSET
    label: Unset | str=UNSET
    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""

        id=self.id

        label=self.label

        field_dict: dict[str, Any]={}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"]=id
        if label is not UNSET:
            field_dict["label"]=label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""

        d=dict(src_dict)
        id=d.pop("id", UNSET)

        label=d.pop("label", UNSET)

        video_constant_string_language=cls(
            id=id, label=label)

        video_constant_string_language.additional_properties=d
        return video_constant_string_language

    @property
    def additional_keys(self) -> list[str]:
        """Get additional property keys."""

        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key]=value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
