from enum import Enum


class VideosForXMLItemEnclosureType(str, Enum):
    APPLICATIONX_BITTORRENT = "application/x-bittorrent"

    def __str__(self) -> str:
        return str(self.value)
