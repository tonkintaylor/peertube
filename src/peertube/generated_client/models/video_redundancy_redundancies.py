from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.file_redundancy_information import FileRedundancyInformation





T = TypeVar("T", bound="VideoRedundancyRedundancies")



@_attrs_define
class VideoRedundancyRedundancies:
    """ 
        Attributes:
            streaming_playlists (Union[Unset, list['FileRedundancyInformation']]):
     """

    streaming_playlists: Union[Unset, list['FileRedundancyInformation']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_redundancy_information import FileRedundancyInformation
        streaming_playlists: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.streaming_playlists, Unset):
            streaming_playlists = []
            for streaming_playlists_item_data in self.streaming_playlists:
                streaming_playlists_item = streaming_playlists_item_data.to_dict()
                streaming_playlists.append(streaming_playlists_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if streaming_playlists is not UNSET:
            field_dict["streamingPlaylists"] = streaming_playlists

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_redundancy_information import FileRedundancyInformation
        d = dict(src_dict)
        streaming_playlists = []
        _streaming_playlists = d.pop("streamingPlaylists", UNSET)
        for streaming_playlists_item_data in (_streaming_playlists or []):
            streaming_playlists_item = FileRedundancyInformation.from_dict(streaming_playlists_item_data)



            streaming_playlists.append(streaming_playlists_item)


        video_redundancy_redundancies = cls(
            streaming_playlists=streaming_playlists,
        )


        video_redundancy_redundancies.additional_properties = d
        return video_redundancy_redundancies

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
