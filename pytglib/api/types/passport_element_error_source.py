

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
    def read(q: dict, *args) -> "PassportElementErrorSourceTranslationFiles or PassportElementErrorSourceDataField or PassportElementErrorSourceFile or PassportElementErrorSourceFrontSide or PassportElementErrorSourceUnspecified or PassportElementErrorSourceSelfie or PassportElementErrorSourceFiles or PassportElementErrorSourceTranslationFile or PassportElementErrorSourceReverseSide":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementErrorSource()
