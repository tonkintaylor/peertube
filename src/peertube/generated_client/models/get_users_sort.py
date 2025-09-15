from enum import Enum

class GetUsersSort(str, Enum):
    VALUE_0 = "-id"
    VALUE_1 = "-username"
    VALUE_2 = "-createdAt"

    def __str__(self) -> str:
        return str(self.value)
