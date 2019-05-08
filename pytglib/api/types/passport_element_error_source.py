

from ..utils import Object


class PassportElementErrorSource(Object):
    """
    Contains the description of an error in a Telegram Passport element

    No parameters required.
    """
    ID = "passportElementErrorSource"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceTranslationFile or PassportElementErrorSourceFile or PassportElementErrorSourceFiles or PassportElementErrorSourceFrontSide or PassportElementErrorSourceUnspecified or PassportElementErrorSourceTranslationFiles or PassportElementErrorSourceSelfie or PassportElementErrorSourceReverseSide or PassportElementErrorSourceDataField":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementErrorSource()
