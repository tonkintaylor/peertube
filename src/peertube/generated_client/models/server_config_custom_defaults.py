from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_custom_defaults_publish import ServerConfigCustomDefaultsPublish
  from ..models.server_config_custom_defaults_p2p import ServerConfigCustomDefaultsP2P
  from ..models.server_config_custom_defaults_player import ServerConfigCustomDefaultsPlayer





T = TypeVar("T", bound="ServerConfigCustomDefaults")



@_attrs_define
class ServerConfigCustomDefaults:
    """ 
        Attributes:
            publish (Union[Unset, ServerConfigCustomDefaultsPublish]):
            p2p (Union[Unset, ServerConfigCustomDefaultsP2P]):
            player (Union[Unset, ServerConfigCustomDefaultsPlayer]):
     """

    publish: Union[Unset, 'ServerConfigCustomDefaultsPublish'] = UNSET
    p2p: Union[Unset, 'ServerConfigCustomDefaultsP2P'] = UNSET
    player: Union[Unset, 'ServerConfigCustomDefaultsPlayer'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_custom_defaults_publish import ServerConfigCustomDefaultsPublish
        from ..models.server_config_custom_defaults_p2p import ServerConfigCustomDefaultsP2P
        from ..models.server_config_custom_defaults_player import ServerConfigCustomDefaultsPlayer
        publish: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.publish, Unset):
            publish = self.publish.to_dict()

        p2p: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.p2p, Unset):
            p2p = self.p2p.to_dict()

        player: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if publish is not UNSET:
            field_dict["publish"] = publish
        if p2p is not UNSET:
            field_dict["p2p"] = p2p
        if player is not UNSET:
            field_dict["player"] = player

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_custom_defaults_publish import ServerConfigCustomDefaultsPublish
        from ..models.server_config_custom_defaults_p2p import ServerConfigCustomDefaultsP2P
        from ..models.server_config_custom_defaults_player import ServerConfigCustomDefaultsPlayer
        d = dict(src_dict)
        _publish = d.pop("publish", UNSET)
        publish: Union[Unset, ServerConfigCustomDefaultsPublish]
        if isinstance(_publish,  Unset):
            publish = UNSET
        else:
            publish = ServerConfigCustomDefaultsPublish.from_dict(_publish)




        _p2p = d.pop("p2p", UNSET)
        p2p: Union[Unset, ServerConfigCustomDefaultsP2P]
        if isinstance(_p2p,  Unset):
            p2p = UNSET
        else:
            p2p = ServerConfigCustomDefaultsP2P.from_dict(_p2p)




        _player = d.pop("player", UNSET)
        player: Union[Unset, ServerConfigCustomDefaultsPlayer]
        if isinstance(_player,  Unset):
            player = UNSET
        else:
            player = ServerConfigCustomDefaultsPlayer.from_dict(_player)




        server_config_custom_defaults = cls(
            publish=publish,
            p2p=p2p,
            player=player,
        )


        server_config_custom_defaults.additional_properties = d
        return server_config_custom_defaults

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
