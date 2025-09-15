from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.video_constant_string_language import VideoConstantStringLanguage





T = TypeVar("T", bound="VideoCaption")



@_attrs_define
class VideoCaption:
    """ 
        Attributes:
            language (Union[Unset, VideoConstantStringLanguage]):
            caption_path (Union[Unset, str]):
     """

    language: Union[Unset, 'VideoConstantStringLanguage'] = UNSET
    caption_path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.video_constant_string_language import VideoConstantStringLanguage
        language: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        caption_path = self.caption_path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if language is not UNSET:
            field_dict["language"] = language
        if caption_path is not UNSET:
            field_dict["captionPath"] = caption_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_constant_string_language import VideoConstantStringLanguage
        d = dict(src_dict)
        _language = d.pop("language", UNSET)
        language: Union[Unset, VideoConstantStringLanguage]
        if isinstance(_language,  Unset):
            language = UNSET
        else:
            language = VideoConstantStringLanguage.from_dict(_language)




        caption_path = d.pop("captionPath", UNSET)

        video_caption = cls(
            language=language,
            caption_path=caption_path,
        )


        video_caption.additional_properties = d
        return video_caption

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
