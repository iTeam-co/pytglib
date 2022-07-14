

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
    def read(q: dict, *args) -> "PassportElementErrorSourceUnspecified or PassportElementErrorSourceTranslationFiles or PassportElementErrorSourceTranslationFile or PassportElementErrorSourceFiles or PassportElementErrorSourceSelfie or PassportElementErrorSourceReverseSide or PassportElementErrorSourceFile or PassportElementErrorSourceFrontSide or PassportElementErrorSourceDataField":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementErrorSource()
