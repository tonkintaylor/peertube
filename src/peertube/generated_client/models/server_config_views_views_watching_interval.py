from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ServerConfigViewsViewsWatchingInterval")



@_attrs_define
class ServerConfigViewsViewsWatchingInterval:
    """ 
        Attributes:
            anonymous (Union[Unset, float]): Milliseconds
            users (Union[Unset, float]): Milliseconds
     """

    anonymous: Union[Unset, float] = UNSET
    users: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        anonymous = self.anonymous

        users = self.users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if anonymous is not UNSET:
            field_dict["anonymous"] = anonymous
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anonymous = d.pop("anonymous", UNSET)

        users = d.pop("users", UNSET)

        server_config_views_views_watching_interval = cls(
            anonymous=anonymous,
            users=users,
        )


        server_config_views_views_watching_interval.additional_properties = d
        return server_config_views_views_watching_interval

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
