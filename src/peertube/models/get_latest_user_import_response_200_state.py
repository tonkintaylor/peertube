from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.models.user_import_state import UserImportState
from peertube.types import UNSET, Unset

T = TypeVar("T", bound="GetLatestUserImportResponse200State")


@_attrs_define
class GetLatestUserImportResponse200State:
    """Attributes:
    id (Union[Unset, UserImportState]): The user import state:
          - `1`: Pending
          - `2`: Processing
          - `3`: Completed
          - `4`: Errored
    label (Union[Unset, str]):
    """

    id: Unset | UserImportState = UNSET
    label: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | int = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Unset | UserImportState
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UserImportState(_id)

        label = d.pop("label", UNSET)

        get_latest_user_import_response_200_state = cls(
            id=id,
            label=label,
        )

        get_latest_user_import_response_200_state.additional_properties = d
        return get_latest_user_import_response_200_state

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
