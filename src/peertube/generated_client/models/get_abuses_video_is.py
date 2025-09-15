from enum import Enum

class GetAbusesVideoIs(str, Enum):
    BLACKLISTED = "blacklisted"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
