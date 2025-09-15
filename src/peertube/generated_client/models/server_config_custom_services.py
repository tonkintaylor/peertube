from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_custom_services_twitter import ServerConfigCustomServicesTwitter





T = TypeVar("T", bound="ServerConfigCustomServices")



@_attrs_define
class ServerConfigCustomServices:
    """ 
        Attributes:
            twitter (Union[Unset, ServerConfigCustomServicesTwitter]):
     """

    twitter: Union[Unset, 'ServerConfigCustomServicesTwitter'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_custom_services_twitter import ServerConfigCustomServicesTwitter
        twitter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.twitter, Unset):
            twitter = self.twitter.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if twitter is not UNSET:
            field_dict["twitter"] = twitter

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_custom_services_twitter import ServerConfigCustomServicesTwitter
        d = dict(src_dict)
        _twitter = d.pop("twitter", UNSET)
        twitter: Union[Unset, ServerConfigCustomServicesTwitter]
        if isinstance(_twitter,  Unset):
            twitter = UNSET
        else:
            twitter = ServerConfigCustomServicesTwitter.from_dict(_twitter)




        server_config_custom_services = cls(
            twitter=twitter,
        )


        server_config_custom_services.additional_properties = d
        return server_config_custom_services

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
