from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="PostApiV1ConfigInstanceAvatarPickBody")



@_attrs_define
class PostApiV1ConfigInstanceAvatarPickBody:
    """ 
        Attributes:
            avatarfile (Union[Unset, File]): The file to upload.
     """

    avatarfile: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avatarfile: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.avatarfile, Unset):
            avatarfile = self.avatarfile.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avatarfile is not UNSET:
            field_dict["avatarfile"] = avatarfile

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.avatarfile, Unset):
            files.append(("avatarfile", self.avatarfile.to_tuple()))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _avatarfile = d.pop("avatarfile", UNSET)
        avatarfile: Union[Unset, File]
        if isinstance(_avatarfile,  Unset):
            avatarfile = UNSET
        else:
            avatarfile = File(
             payload = BytesIO(_avatarfile)
        )




        post_api_v1_config_instance_avatar_pick_body = cls(
            avatarfile=avatarfile,
        )


        post_api_v1_config_instance_avatar_pick_body.additional_properties = d
        return post_api_v1_config_instance_avatar_pick_body

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
