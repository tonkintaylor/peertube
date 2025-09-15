from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.o_auth_token_refresh_token_grant_type import OAuthTokenRefreshTokenGrantType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="OAuthTokenRefreshToken")



@_attrs_define
class OAuthTokenRefreshToken:
    """ 
        Attributes:
            grant_type (OAuthTokenRefreshTokenGrantType):  Default: OAuthTokenRefreshTokenGrantType.PASSWORD.
            refresh_token (str):  Example: 2e0d675df9fc96d2e4ec8a3ebbbf45eca9137bb7.
            client_id (Union[Unset, str]):  Example: v1ikx5hnfop4mdpnci8nsqh93c45rldf.
            client_secret (Union[Unset, str]):  Example: AjWiOapPltI6EnsWQwlFarRtLh4u8tDt.
     """

    refresh_token: str
    grant_type: OAuthTokenRefreshTokenGrantType = OAuthTokenRefreshTokenGrantType.PASSWORD
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        refresh_token = self.refresh_token

        client_id = self.client_id

        client_secret = self.client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "grant_type": grant_type,
            "refresh_token": refresh_token,
        })
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = OAuthTokenRefreshTokenGrantType(d.pop("grant_type"))




        refresh_token = d.pop("refresh_token")

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        o_auth_token_refresh_token = cls(
            grant_type=grant_type,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
        )


        o_auth_token_refresh_token.additional_properties = d
        return o_auth_token_refresh_token

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
