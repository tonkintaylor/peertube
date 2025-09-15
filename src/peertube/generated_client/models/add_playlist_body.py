from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..models.video_playlist_privacy_set import VideoPlaylistPrivacySet
from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="AddPlaylistBody")



@_attrs_define
class AddPlaylistBody:
    """ 
        Attributes:
            display_name (str): Video playlist display name
            thumbnailfile (Union[Unset, File]): Video playlist thumbnail file
            privacy (Union[Unset, VideoPlaylistPrivacySet]): Video playlist privacy policy (see [/video-
                playlists/privacies](#operation/getPlaylistPrivacyPolicies))
            description (Union[Unset, str]): Video playlist description
            video_channel_id (Union[Unset, int]):  Example: 42.
     """

    display_name: str
    thumbnailfile: Union[Unset, File] = UNSET
    privacy: Union[Unset, VideoPlaylistPrivacySet] = UNSET
    description: Union[Unset, str] = UNSET
    video_channel_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        thumbnailfile: Union[Unset, FileTypes] = UNSET
        if not isinstance(self.thumbnailfile, Unset):
            thumbnailfile = self.thumbnailfile.to_tuple()


        privacy: Union[Unset, int] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value


        description = self.description

        video_channel_id = self.video_channel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "displayName": display_name,
        })
        if thumbnailfile is not UNSET:
            field_dict["thumbnailfile"] = thumbnailfile
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if description is not UNSET:
            field_dict["description"] = description
        if video_channel_id is not UNSET:
            field_dict["videoChannelId"] = video_channel_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("displayName", (None, str(self.display_name).encode(), "text/plain")))



        if not isinstance(self.thumbnailfile, Unset):
            files.append(("thumbnailfile", self.thumbnailfile.to_tuple()))



        if not isinstance(self.privacy, Unset):
            files.append(("privacy",  (None, str(self.privacy.value).encode(), "text/plain")))



        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))



        if not isinstance(self.video_channel_id, Unset):
            files.append(("videoChannelId", (None, str(self.video_channel_id).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName")

        _thumbnailfile = d.pop("thumbnailfile", UNSET)
        thumbnailfile: Union[Unset, File]
        if isinstance(_thumbnailfile,  Unset):
            thumbnailfile = UNSET
        else:
            thumbnailfile = File(
             payload = BytesIO(_thumbnailfile)
        )




        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, VideoPlaylistPrivacySet]
        if isinstance(_privacy,  Unset):
            privacy = UNSET
        else:
            privacy = VideoPlaylistPrivacySet(_privacy)




        description = d.pop("description", UNSET)

        video_channel_id = d.pop("videoChannelId", UNSET)

        add_playlist_body = cls(
            display_name=display_name,
            thumbnailfile=thumbnailfile,
            privacy=privacy,
            description=description,
            video_channel_id=video_channel_id,
        )


        add_playlist_body.additional_properties = d
        return add_playlist_body

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
