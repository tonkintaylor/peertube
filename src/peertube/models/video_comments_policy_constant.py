from collections.abc import Mapping
from typing import (
    Any, TypeVar)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.models.video_comments_policy_set import VideoCommentsPolicySet
from peertube.types import UNSET, Unset

T=TypeVar("T", bound="VideoCommentsPolicyConstant")


@_attrs_define
class VideoCommentsPolicyConstant:
    """Attributes:
    id (Union[Unset, VideoCommentsPolicySet]): Comments policy of the video (Enabled=`1`, Disabled=`2`, Requires
        Approval=`3`)
    label (Union[Unset, str]):
    """


    id: Unset | VideoCommentsPolicySet=UNSET
    label: Unset | str=UNSET
    additional_properties: dict[str, Any]=_attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert instance to dictionary."""

        id: Unset | int=UNSET
        if not isinstance(self.id, Unset):
            id=self.id.value

        label=self.label

        field_dict: dict[str, Any]={}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"]=id
        if label is not UNSET:
            field_dict["label"]=label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create instance from dictionary."""

        d=dict(src_dict)
        _id=d.pop("id", UNSET)
        id: Unset | VideoCommentsPolicySet
        if isinstance(_id, Unset):
            id=UNSET
        else:
            id=VideoCommentsPolicySet(_id)

        label=d.pop("label", UNSET)

        video_comments_policy_constant=cls(
            id=id, label=label)

        video_comments_policy_constant.additional_properties=d
        return video_comments_policy_constant

    @property
    def additional_keys(self) -> list[str]:
        """Get additional property keys."""

        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key]=value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
