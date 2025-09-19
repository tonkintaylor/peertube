from collections.abc import Mapping
from typing import (
    Any, TypeVar)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T=TypeVar("T", bound="Cut")


@_attrs_define
class Cut:
    """Attributes:"""


    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""

        field_dict: dict[str, Any]={}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""

        d=dict(src_dict)
        cut=cls()
        cut.additional_properties=d
        return cut

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
