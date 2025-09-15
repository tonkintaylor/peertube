from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyUserBody")


@_attrs_define
class VerifyUserBody:
    """Attributes:
    verification_string (str):
    is_pending_email (Union[Unset, bool]):
    """

    verification_string: str
    is_pending_email: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verification_string = self.verification_string

        is_pending_email = self.is_pending_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verificationString": verification_string,
            }
        )
        if is_pending_email is not UNSET:
            field_dict["isPendingEmail"] = is_pending_email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        verification_string = d.pop("verificationString")

        is_pending_email = d.pop("isPendingEmail", UNSET)

        verify_user_body = cls(
            verification_string=verification_string,
            is_pending_email=is_pending_email,
        )

        verify_user_body.additional_properties = d
        return verify_user_body

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
