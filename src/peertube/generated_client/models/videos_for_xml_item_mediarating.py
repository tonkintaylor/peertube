from enum import Enum

class VideosForXMLItemMediarating(str, Enum):
    ADULT = "adult"
    NONADULT = "nonadult"

    def __str__(self) -> str:
        return str(self.value)
