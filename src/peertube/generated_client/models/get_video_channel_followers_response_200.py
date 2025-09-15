from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.follow import Follow





T = TypeVar("T", bound="GetVideoChannelFollowersResponse200")



@_attrs_define
class GetVideoChannelFollowersResponse200:
    """ 
        Attributes:
            total (Union[Unset, int]):  Example: 1.
            data (Union[Unset, list['Follow']]):
     """

    total: Union[Unset, int] = UNSET
    data: Union[Unset, list['Follow']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.follow import Follow
        total = self.total

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.follow import Follow
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in (_data or []):
            data_item = Follow.from_dict(data_item_data)



            data.append(data_item)


        get_video_channel_followers_response_200 = cls(
            total=total,
            data=data,
        )


        get_video_channel_followers_response_200.additional_properties = d
        return get_video_channel_followers_response_200

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
