from enum import Enum

class AutomaticTagAvailableAvailableItemType(str, Enum):
    CORE = "core"
    WATCHED_WORDS_LIST = "watched-words-list"

    def __str__(self) -> str:
        return str(self.value)
