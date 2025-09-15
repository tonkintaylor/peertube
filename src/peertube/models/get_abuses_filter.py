from enum import Enum


class GetAbusesFilter(str, Enum):
    ACCOUNT = "account"
    COMMENT = "comment"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
