from enum import Enum


class PutApiV1VideosIdRateBodyRating(str, Enum):
    DISLIKE = "dislike"
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
