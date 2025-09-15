from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_export_users import ServerConfigExportUsers





T = TypeVar("T", bound="ServerConfigExport")



@_attrs_define
class ServerConfigExport:
    """ 
        Attributes:
            users (Union[Unset, ServerConfigExportUsers]):
     """

    users: Union[Unset, 'ServerConfigExportUsers'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_export_users import ServerConfigExportUsers
        users: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_export_users import ServerConfigExportUsers
        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: Union[Unset, ServerConfigExportUsers]
        if isinstance(_users,  Unset):
            users = UNSET
        else:
            users = ServerConfigExportUsers.from_dict(_users)




        server_config_export = cls(
            users=users,
        )


        server_config_export.additional_properties = d
        return server_config_export

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
