from enum import Enum


class SearchChannelsSearchTarget(str, Enum):
    LOCAL = "local"
    SEARCH_INDEX = "search-index"

    def __str__(self) -> str:
        return str(self.value)
