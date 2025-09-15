from enum import Enum


class GetApiV1ServerFollowingActorType(str, Enum):
    APPLICATION = "Application"
    GROUP = "Group"
    ORGANIZATION = "Organization"
    PERSON = "Person"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
