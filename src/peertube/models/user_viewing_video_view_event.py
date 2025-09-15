from enum import Enum


class UserViewingVideoViewEvent(str, Enum):
    SEEK = "seek"

    def __str__(self) -> str:
        return str(self.value)
