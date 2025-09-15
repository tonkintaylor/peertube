from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_custom_defaults_p2p_webapp import ServerConfigCustomDefaultsP2PWebapp
  from ..models.server_config_custom_defaults_p2p_embed import ServerConfigCustomDefaultsP2PEmbed





T = TypeVar("T", bound="ServerConfigCustomDefaultsP2P")



@_attrs_define
class ServerConfigCustomDefaultsP2P:
    """ 
        Attributes:
            webapp (Union[Unset, ServerConfigCustomDefaultsP2PWebapp]):
            embed (Union[Unset, ServerConfigCustomDefaultsP2PEmbed]):
     """

    webapp: Union[Unset, 'ServerConfigCustomDefaultsP2PWebapp'] = UNSET
    embed: Union[Unset, 'ServerConfigCustomDefaultsP2PEmbed'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_custom_defaults_p2p_webapp import ServerConfigCustomDefaultsP2PWebapp
        from ..models.server_config_custom_defaults_p2p_embed import ServerConfigCustomDefaultsP2PEmbed
        webapp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.webapp, Unset):
            webapp = self.webapp.to_dict()

        embed: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.embed, Unset):
            embed = self.embed.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if webapp is not UNSET:
            field_dict["webapp"] = webapp
        if embed is not UNSET:
            field_dict["embed"] = embed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_custom_defaults_p2p_webapp import ServerConfigCustomDefaultsP2PWebapp
        from ..models.server_config_custom_defaults_p2p_embed import ServerConfigCustomDefaultsP2PEmbed
        d = dict(src_dict)
        _webapp = d.pop("webapp", UNSET)
        webapp: Union[Unset, ServerConfigCustomDefaultsP2PWebapp]
        if isinstance(_webapp,  Unset):
            webapp = UNSET
        else:
            webapp = ServerConfigCustomDefaultsP2PWebapp.from_dict(_webapp)




        _embed = d.pop("embed", UNSET)
        embed: Union[Unset, ServerConfigCustomDefaultsP2PEmbed]
        if isinstance(_embed,  Unset):
            embed = UNSET
        else:
            embed = ServerConfigCustomDefaultsP2PEmbed.from_dict(_embed)




        server_config_custom_defaults_p2p = cls(
            webapp=webapp,
            embed=embed,
        )


        server_config_custom_defaults_p2p.additional_properties = d
        return server_config_custom_defaults_p2p

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
