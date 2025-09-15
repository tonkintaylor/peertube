from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.post_api_v1_abuses_response_200_abuse import PostApiV1AbusesResponse200Abuse





T = TypeVar("T", bound="PostApiV1AbusesResponse200")



@_attrs_define
class PostApiV1AbusesResponse200:
    """ 
        Attributes:
            abuse (Union[Unset, PostApiV1AbusesResponse200Abuse]):
     """

    abuse: Union[Unset, 'PostApiV1AbusesResponse200Abuse'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_api_v1_abuses_response_200_abuse import PostApiV1AbusesResponse200Abuse
        abuse: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.abuse, Unset):
            abuse = self.abuse.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if abuse is not UNSET:
            field_dict["abuse"] = abuse

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_abuses_response_200_abuse import PostApiV1AbusesResponse200Abuse
        d = dict(src_dict)
        _abuse = d.pop("abuse", UNSET)
        abuse: Union[Unset, PostApiV1AbusesResponse200Abuse]
        if isinstance(_abuse,  Unset):
            abuse = UNSET
        else:
            abuse = PostApiV1AbusesResponse200Abuse.from_dict(_abuse)




        post_api_v1_abuses_response_200 = cls(
            abuse=abuse,
        )


        post_api_v1_abuses_response_200.additional_properties = d
        return post_api_v1_abuses_response_200

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
