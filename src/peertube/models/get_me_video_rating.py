from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from peertube.models.get_me_video_rating_rating import GetMeVideoRatingRating

T = TypeVar("T", bound="GetMeVideoRating")


@_attrs_define
class GetMeVideoRating:
    """Attributes:
    id (int):  Example: 42.
    rating (GetMeVideoRatingRating): Rating of the video
    """

    id: int
    rating: GetMeVideoRatingRating
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rating = self.rating.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rating": rating,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        rating = GetMeVideoRatingRating(d.pop("rating"))

        get_me_video_rating = cls(
            id=id,
            rating=rating,
        )

        get_me_video_rating.additional_properties = d
        return get_me_video_rating

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
