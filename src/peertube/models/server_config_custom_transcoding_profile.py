from enum import Enum


class ServerConfigCustomTranscodingProfile(str, Enum):
    DEFAULT = "default"

    def __str__(self) -> str:
        return str(self.value)
