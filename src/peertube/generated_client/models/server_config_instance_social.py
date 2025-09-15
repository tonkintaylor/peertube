from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ServerConfigInstanceSocial")



@_attrs_define
class ServerConfigInstanceSocial:
    """ 
        Attributes:
            external_link (Union[Unset, str]):
            mastodon_link (Union[Unset, str]):
            bluesky_link (Union[Unset, str]):
            x_link (Union[Unset, str]):
     """

    external_link: Union[Unset, str] = UNSET
    mastodon_link: Union[Unset, str] = UNSET
    bluesky_link: Union[Unset, str] = UNSET
    x_link: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_link = self.external_link

        mastodon_link = self.mastodon_link

        bluesky_link = self.bluesky_link

        x_link = self.x_link


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if external_link is not UNSET:
            field_dict["externalLink"] = external_link
        if mastodon_link is not UNSET:
            field_dict["mastodonLink"] = mastodon_link
        if bluesky_link is not UNSET:
            field_dict["blueskyLink"] = bluesky_link
        if x_link is not UNSET:
            field_dict["xLink"] = x_link

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_link = d.pop("externalLink", UNSET)

        mastodon_link = d.pop("mastodonLink", UNSET)

        bluesky_link = d.pop("blueskyLink", UNSET)

        x_link = d.pop("xLink", UNSET)

        server_config_instance_social = cls(
            external_link=external_link,
            mastodon_link=mastodon_link,
            bluesky_link=bluesky_link,
            x_link=x_link,
        )


        server_config_instance_social.additional_properties = d
        return server_config_instance_social

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
