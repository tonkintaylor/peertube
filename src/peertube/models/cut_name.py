from enum import Enum


class CutName(str, Enum):
    CUT = "cut"

    def __str__(self) -> str:
        return str(self.value)
