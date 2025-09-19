from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T=TypeVar("T", bound="PluginSettings")


@_attrs_define
class PluginSettings:
    """Data model."""


    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""

        field_dict: dict[str, Any]={}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create from dictionary."""

        d=dict(src_dict)
        plugin_settings=cls()

        plugin_settings.additional_properties=d
        return plugin_settings

    @property
    def additional_keys(self) -> list[str]:
        """Get additional keys."""

        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key]=value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
