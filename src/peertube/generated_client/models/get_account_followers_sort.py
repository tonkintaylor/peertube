from enum import Enum

class GetAccountFollowersSort(str, Enum):
    CREATEDAT = "createdAt"

    def __str__(self) -> str:
        return str(self.value)
