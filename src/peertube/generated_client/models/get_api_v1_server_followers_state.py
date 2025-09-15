from enum import Enum

class GetApiV1ServerFollowersState(str, Enum):
    ACCEPTED = "accepted"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
