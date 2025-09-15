from enum import Enum

class DeleteApiV1ConfigInstanceLogoLogoTypeLogoType(str, Enum):
    FAVICON = "favicon"
    HEADER_SQUARE = "header-square"
    HEADER_WIDE = "header-wide"
    OPENGRAPH = "opengraph"

    def __str__(self) -> str:
        return str(self.value)
