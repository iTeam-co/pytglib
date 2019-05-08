

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
    def read(q: dict, *args) -> "InputPassportElementErrorSourceSelfie or InputPassportElementErrorSourceDataField or InputPassportElementErrorSourceFile or InputPassportElementErrorSourceReverseSide or InputPassportElementErrorSourceTranslationFile or InputPassportElementErrorSourceFiles or InputPassportElementErrorSourceFrontSide or InputPassportElementErrorSourceTranslationFiles or InputPassportElementErrorSourceUnspecified":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElementErrorSource()
