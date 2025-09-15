from enum import Enum

class CreateVideoTranscodingBodyTranscodingType(str, Enum):
    HLS = "hls"
    WEB_VIDEO = "web-video"

    def __str__(self) -> str:
        return str(self.value)
