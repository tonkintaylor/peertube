from collections.abc import Mapping
from typing import (
    TYPE_CHECKING, Any, TypeVar, Union)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.types import UNSET, Unset

if TYPE_CHECKING:
    from peertube.models.video_chapters_chapters import VideoChaptersChapters


T=TypeVar("T", bound="VideoChapters")


@_attrs_define
class VideoChapters:
    """Attributes:
    chapters (Union[Unset, VideoChaptersChapters]):
    """


    chapters: Union[Unset, "VideoChaptersChapters"]=UNSET
    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""

        chapters: Unset | dict[str, Any]=UNSET
        if not isinstance(self.chapters, Unset):
            chapters=self.chapters.to_dict()

        field_dict: dict[str, Any]={}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chapters is not UNSET:
            field_dict["chapters"]=chapters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""

        from peertube.models.video_chapters_chapters import VideoChaptersChapters

        d=dict(src_dict)
        _chapters=d.pop("chapters", UNSET)
        chapters: Unset | VideoChaptersChapters
        if isinstance(_chapters, Unset):
            chapters=UNSET
        else:
            chapters=VideoChaptersChapters.from_dict(_chapters)

        video_chapters=cls(
            chapters=chapters)

        video_chapters.additional_properties=d
        return video_chapters

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
