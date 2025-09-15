from enum import Enum

class GetApiV1RunnersSort(str, Enum):
    CREATEDAT = "createdAt"

    def __str__(self) -> str:
        return str(self.value)
