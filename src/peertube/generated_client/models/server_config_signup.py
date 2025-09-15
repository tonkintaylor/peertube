from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ServerConfigSignup")



@_attrs_define
class ServerConfigSignup:
    """ 
        Attributes:
            allowed (Union[Unset, bool]):
            allowed_for_current_ip (Union[Unset, bool]):
            requires_email_verification (Union[Unset, bool]):
     """

    allowed: Union[Unset, bool] = UNSET
    allowed_for_current_ip: Union[Unset, bool] = UNSET
    requires_email_verification: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        allowed_for_current_ip = self.allowed_for_current_ip

        requires_email_verification = self.requires_email_verification


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if allowed_for_current_ip is not UNSET:
            field_dict["allowedForCurrentIP"] = allowed_for_current_ip
        if requires_email_verification is not UNSET:
            field_dict["requiresEmailVerification"] = requires_email_verification

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed", UNSET)

        allowed_for_current_ip = d.pop("allowedForCurrentIP", UNSET)

        requires_email_verification = d.pop("requiresEmailVerification", UNSET)

        server_config_signup = cls(
            allowed=allowed,
            allowed_for_current_ip=allowed_for_current_ip,
            requires_email_verification=requires_email_verification,
        )


        server_config_signup.additional_properties = d
        return server_config_signup

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
