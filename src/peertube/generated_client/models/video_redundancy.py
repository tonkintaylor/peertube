from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.video_redundancy_redundancies import VideoRedundancyRedundancies





T = TypeVar("T", bound="VideoRedundancy")



@_attrs_define
class VideoRedundancy:
    """ 
        Attributes:
            id (Union[Unset, int]):  Example: 42.
            name (Union[Unset, str]):
            url (Union[Unset, str]):
            uuid (Union[Unset, UUID]):  Example: 9c9de5e8-0a1e-484a-b099-e80766180a6d.
            redundancies (Union[Unset, VideoRedundancyRedundancies]):
     """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    uuid: Union[Unset, UUID] = UNSET
    redundancies: Union[Unset, 'VideoRedundancyRedundancies'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.video_redundancy_redundancies import VideoRedundancyRedundancies
        id = self.id

        name = self.name

        url = self.url

        uuid: Union[Unset, str] = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        redundancies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.redundancies, Unset):
            redundancies = self.redundancies.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if redundancies is not UNSET:
            field_dict["redundancies"] = redundancies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_redundancy_redundancies import VideoRedundancyRedundancies
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: Union[Unset, UUID]
        if isinstance(_uuid,  Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)




        _redundancies = d.pop("redundancies", UNSET)
        redundancies: Union[Unset, VideoRedundancyRedundancies]
        if isinstance(_redundancies,  Unset):
            redundancies = UNSET
        else:
            redundancies = VideoRedundancyRedundancies.from_dict(_redundancies)




        video_redundancy = cls(
            id=id,
            name=name,
            url=url,
            uuid=uuid,
            redundancies=redundancies,
        )


        video_redundancy.additional_properties = d
        return video_redundancy

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
