from enum import Enum

class AddOutroName(str, Enum):
    ADD_OUTRO = "add-outro"

    def __str__(self) -> str:
        return str(self.value)
