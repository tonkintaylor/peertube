from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ServerConfigCustomTranscodingResolutions")



@_attrs_define
class ServerConfigCustomTranscodingResolutions:
    """ Resolutions to transcode _new videos_ to

        Attributes:
            0p (Union[Unset, bool]):
            144p (Union[Unset, bool]):
            240p (Union[Unset, bool]):
            360p (Union[Unset, bool]):
            480p (Union[Unset, bool]):
            720p (Union[Unset, bool]):
            1080p (Union[Unset, bool]):
            1440p (Union[Unset, bool]):
            2160p (Union[Unset, bool]):
     """

    0p: Union[Unset, bool] = UNSET
    144p: Union[Unset, bool] = UNSET
    240p: Union[Unset, bool] = UNSET
    360p: Union[Unset, bool] = UNSET
    480p: Union[Unset, bool] = UNSET
    720p: Union[Unset, bool] = UNSET
    1080p: Union[Unset, bool] = UNSET
    1440p: Union[Unset, bool] = UNSET
    2160p: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        0p = self.0p

        144p = self.144p

        240p = self.240p

        360p = self.360p

        480p = self.480p

        720p = self.720p

        1080p = self.1080p

        1440p = self.1440p

        2160p = self.2160p


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if 0p is not UNSET:
            field_dict["0p"] = 0p
        if 144p is not UNSET:
            field_dict["144p"] = 144p
        if 240p is not UNSET:
            field_dict["240p"] = 240p
        if 360p is not UNSET:
            field_dict["360p"] = 360p
        if 480p is not UNSET:
            field_dict["480p"] = 480p
        if 720p is not UNSET:
            field_dict["720p"] = 720p
        if 1080p is not UNSET:
            field_dict["1080p"] = 1080p
        if 1440p is not UNSET:
            field_dict["1440p"] = 1440p
        if 2160p is not UNSET:
            field_dict["2160p"] = 2160p

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        0p = d.pop("0p", UNSET)

        144p = d.pop("144p", UNSET)

        240p = d.pop("240p", UNSET)

        360p = d.pop("360p", UNSET)

        480p = d.pop("480p", UNSET)

        720p = d.pop("720p", UNSET)

        1080p = d.pop("1080p", UNSET)

        1440p = d.pop("1440p", UNSET)

        2160p = d.pop("2160p", UNSET)

        server_config_custom_transcoding_resolutions = cls(
            0p=0p,
            144p=144p,
            240p=240p,
            360p=360p,
            480p=480p,
            720p=720p,
            1080p=1080p,
            1440p=1440p,
            2160p=2160p,
        )


        server_config_custom_transcoding_resolutions.additional_properties = d
        return server_config_custom_transcoding_resolutions

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
