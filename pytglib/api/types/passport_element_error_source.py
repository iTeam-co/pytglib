

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
    def read(q: dict, *args) -> "PassportElementErrorSourceSelfie or PassportElementErrorSourceFrontSide or PassportElementErrorSourceFiles or PassportElementErrorSourceReverseSide or PassportElementErrorSourceUnspecified or PassportElementErrorSourceTranslationFile or PassportElementErrorSourceFile or PassportElementErrorSourceDataField or PassportElementErrorSourceTranslationFiles":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementErrorSource()
