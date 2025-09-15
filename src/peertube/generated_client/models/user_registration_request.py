from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.register_user_channel import RegisterUserChannel





T = TypeVar("T", bound="UserRegistrationRequest")



@_attrs_define
class UserRegistrationRequest:
    """ 
        Attributes:
            username (str): immutable name of the user, used to find or mention its actor Example: chocobozzz.
            password (str):
            email (str): email of the user, used for login or service communications
            registration_reason (str): reason for the user to register on the instance
            display_name (Union[Unset, str]): editable name of the user, displayed in its representations
            channel (Union[Unset, RegisterUserChannel]): channel base information used to create the first channel of the
                user
     """

    username: str
    password: str
    email: str
    registration_reason: str
    display_name: Union[Unset, str] = UNSET
    channel: Union[Unset, 'RegisterUserChannel'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_user_channel import RegisterUserChannel
        username = self.username

        password = self.password

        email = self.email

        registration_reason = self.registration_reason

        display_name = self.display_name

        channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "password": password,
            "email": email,
            "registrationReason": registration_reason,
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_user_channel import RegisterUserChannel
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        email = d.pop("email")

        registration_reason = d.pop("registrationReason")

        display_name = d.pop("displayName", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, RegisterUserChannel]
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = RegisterUserChannel.from_dict(_channel)




        user_registration_request = cls(
            username=username,
            password=password,
            email=email,
            registration_reason=registration_reason,
            display_name=display_name,
            channel=channel,
        )


        user_registration_request.additional_properties = d
        return user_registration_request

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
