from enum import Enum


class PredefinedAbuseReasonsItem(str, Enum):
    CAPTIONS = "captions"
    HATEFULORABUSIVE = "hatefulOrAbusive"
    PRIVACY = "privacy"
    RIGHTS = "rights"
    SERVERRULES = "serverRules"
    SPAMORMISLEADING = "spamOrMisleading"
    THUMBNAILS = "thumbnails"
    VIOLENTORABUSIVE = "violentOrAbusive"

    def __str__(self) -> str:
        return str(self.value)
