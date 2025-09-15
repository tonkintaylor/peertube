from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.replace_video_chapters_body_chapters_item import ReplaceVideoChaptersBodyChaptersItem





T = TypeVar("T", bound="ReplaceVideoChaptersBody")



@_attrs_define
class ReplaceVideoChaptersBody:
    """ 
        Attributes:
            chapters (Union[Unset, list['ReplaceVideoChaptersBodyChaptersItem']]):
     """

    chapters: Union[Unset, list['ReplaceVideoChaptersBodyChaptersItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.replace_video_chapters_body_chapters_item import ReplaceVideoChaptersBodyChaptersItem
        chapters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.chapters, Unset):
            chapters = []
            for chapters_item_data in self.chapters:
                chapters_item = chapters_item_data.to_dict()
                chapters.append(chapters_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chapters is not UNSET:
            field_dict["chapters"] = chapters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replace_video_chapters_body_chapters_item import ReplaceVideoChaptersBodyChaptersItem
        d = dict(src_dict)
        chapters = []
        _chapters = d.pop("chapters", UNSET)
        for chapters_item_data in (_chapters or []):
            chapters_item = ReplaceVideoChaptersBodyChaptersItem.from_dict(chapters_item_data)



            chapters.append(chapters_item)


        replace_video_chapters_body = cls(
            chapters=chapters,
        )


        replace_video_chapters_body.additional_properties = d
        return replace_video_chapters_body

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
