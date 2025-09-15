from enum import Enum

class GetMeVideoRatingRating(str, Enum):
    DISLIKE = "dislike"
    LIKE = "like"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
