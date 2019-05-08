

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
    def read(q: dict, *args) -> "InputPassportElementErrorSourceTranslationFiles or InputPassportElementErrorSourceTranslationFile or InputPassportElementErrorSourceFiles or InputPassportElementErrorSourceReverseSide or InputPassportElementErrorSourceDataField or InputPassportElementErrorSourceSelfie or InputPassportElementErrorSourceFile or InputPassportElementErrorSourceUnspecified or InputPassportElementErrorSourceFrontSide":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElementErrorSource()
