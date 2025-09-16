from collections.abc import Mapping
from io import BytesIO
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube import types
from peertube.types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="AddVideoCaptionBody")


@_attrs_define
class AddVideoCaptionBody:
    """Attributes:
    captionfile (Union[Unset, File]): The file to upload.
    """

    captionfile: Unset | File = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        captionfile: Unset | FileTypes = UNSET
        if not isinstance(self.captionfile, Unset):
            captionfile = self.captionfile.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captionfile is not UNSET:
            field_dict["captionfile"] = captionfile

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.captionfile, Unset):
            files.append(("captionfile", self.captionfile.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create from dictionary."""
        d = dict(src_dict)
        _captionfile = d.pop("captionfile", UNSET)
        captionfile: Unset | File
        if isinstance(_captionfile, Unset):
            captionfile = UNSET
        else:
            captionfile = File(payload=BytesIO(_captionfile))

        add_video_caption_body = cls(
            captionfile=captionfile,
        )

        add_video_caption_body.additional_properties = d
        return add_video_caption_body

    @property
    def additional_keys(self) -> list[str]:
        """Get additional keys."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
