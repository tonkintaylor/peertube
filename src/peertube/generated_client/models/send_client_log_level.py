from enum import Enum

class SendClientLogLevel(str, Enum):
    ERROR = "error"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
