from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="VODAudioMergeTranscoding")



@_attrs_define
class VODAudioMergeTranscoding:
    """ 
        Attributes:
            video_file (Union[Unset, File]):
     """

    video_file: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        video_file: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.video_file, Unset):
            video_file = self.video_file.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if video_file is not UNSET:
            field_dict["videoFile"] = video_file

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _video_file = d.pop("videoFile", UNSET)
        video_file: Union[Unset, File]
        if isinstance(_video_file,  Unset):
            video_file = UNSET
        else:
            video_file = File(
             payload = BytesIO(_video_file)
        )




        vod_audio_merge_transcoding = cls(
            video_file=video_file,
        )


        vod_audio_merge_transcoding.additional_properties = d
        return vod_audio_merge_transcoding

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
