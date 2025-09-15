from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.video_comments_policy_set import VideoCommentsPolicySet
from ..models.video_privacy_set import VideoPrivacySet
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ServerConfigCustomDefaultsPublish")



@_attrs_define
class ServerConfigCustomDefaultsPublish:
    """ 
        Attributes:
            download_enabled (Union[Unset, bool]):
            comments_policy (Union[Unset, VideoCommentsPolicySet]): Comments policy of the video (Enabled = `1`, Disabled =
                `2`, Requires Approval = `3`)
            privacy (Union[Unset, VideoPrivacySet]): privacy id of the video (see
                [/videos/privacies](#operation/getVideoPrivacyPolicies))
            licence (Union[Unset, int]): licence id of the video (see [/videos/licences](#operation/getLicences)) Example:
                2.
     """

    download_enabled: Union[Unset, bool] = UNSET
    comments_policy: Union[Unset, VideoCommentsPolicySet] = UNSET
    privacy: Union[Unset, VideoPrivacySet] = UNSET
    licence: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        download_enabled = self.download_enabled

        comments_policy: Union[Unset, int] = UNSET
        if not isinstance(self.comments_policy, Unset):
            comments_policy = self.comments_policy.value


        privacy: Union[Unset, int] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value


        licence = self.licence


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if download_enabled is not UNSET:
            field_dict["downloadEnabled"] = download_enabled
        if comments_policy is not UNSET:
            field_dict["commentsPolicy"] = comments_policy
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if licence is not UNSET:
            field_dict["licence"] = licence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_enabled = d.pop("downloadEnabled", UNSET)

        _comments_policy = d.pop("commentsPolicy", UNSET)
        comments_policy: Union[Unset, VideoCommentsPolicySet]
        if isinstance(_comments_policy,  Unset):
            comments_policy = UNSET
        else:
            comments_policy = VideoCommentsPolicySet(_comments_policy)




        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, VideoPrivacySet]
        if isinstance(_privacy,  Unset):
            privacy = UNSET
        else:
            privacy = VideoPrivacySet(_privacy)




        licence = d.pop("licence", UNSET)

        server_config_custom_defaults_publish = cls(
            download_enabled=download_enabled,
            comments_policy=comments_policy,
            privacy=privacy,
            licence=licence,
        )


        server_config_custom_defaults_publish.additional_properties = d
        return server_config_custom_defaults_publish

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
