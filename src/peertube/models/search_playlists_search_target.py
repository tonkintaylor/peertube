from enum import Enum


class SearchPlaylistsSearchTarget(str, Enum):
    """SearchPlaylistsSearchTarget enumeration."""
    LOCAL = "local"
    SEARCH_INDEX = "search-index"

    def __str__(self) -> str:
        return str(self.value)
