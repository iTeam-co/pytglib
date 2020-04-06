

from ..utils import Object


class InputPassportElementErrorSource(Object):
    """
    Contains the description of an error in a Telegram Passport element; for bots only

    No parameters required.
    """
    ID = "inputPassportElementErrorSource"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceDataField or InputPassportElementErrorSourceSelfie or InputPassportElementErrorSourceTranslationFiles or InputPassportElementErrorSourceReverseSide or InputPassportElementErrorSourceFrontSide or InputPassportElementErrorSourceFile or InputPassportElementErrorSourceFiles or InputPassportElementErrorSourceTranslationFile or InputPassportElementErrorSourceUnspecified":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElementErrorSource()
