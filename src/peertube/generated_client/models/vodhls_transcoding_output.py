from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="VODHLSTranscodingOutput")



@_attrs_define
class VODHLSTranscodingOutput:
    """ 
        Attributes:
            resolution (Union[Unset, float]):
            fps (Union[Unset, float]):
     """

    resolution: Union[Unset, float] = UNSET
    fps: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        resolution = self.resolution

        fps = self.fps


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if fps is not UNSET:
            field_dict["fps"] = fps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolution = d.pop("resolution", UNSET)

        fps = d.pop("fps", UNSET)

        vodhls_transcoding_output = cls(
            resolution=resolution,
            fps=fps,
        )


        vodhls_transcoding_output.additional_properties = d
        return vodhls_transcoding_output

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
