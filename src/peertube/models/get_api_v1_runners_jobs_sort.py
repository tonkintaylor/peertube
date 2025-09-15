from enum import Enum


class GetApiV1RunnersJobsSort(str, Enum):
    CREATEDAT = "createdAt"
    PRIORITY = "priority"
    PROGRESS = "progress"
    STATE = "state"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
