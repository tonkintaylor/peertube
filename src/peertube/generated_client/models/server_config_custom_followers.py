from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_custom_followers_instance import ServerConfigCustomFollowersInstance





T = TypeVar("T", bound="ServerConfigCustomFollowers")



@_attrs_define
class ServerConfigCustomFollowers:
    """ 
        Attributes:
            instance (Union[Unset, ServerConfigCustomFollowersInstance]):
     """

    instance: Union[Unset, 'ServerConfigCustomFollowersInstance'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_custom_followers_instance import ServerConfigCustomFollowersInstance
        instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_custom_followers_instance import ServerConfigCustomFollowersInstance
        d = dict(src_dict)
        _instance = d.pop("instance", UNSET)
        instance: Union[Unset, ServerConfigCustomFollowersInstance]
        if isinstance(_instance,  Unset):
            instance = UNSET
        else:
            instance = ServerConfigCustomFollowersInstance.from_dict(_instance)




        server_config_custom_followers = cls(
            instance=instance,
        )


        server_config_custom_followers.additional_properties = d
        return server_config_custom_followers

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
