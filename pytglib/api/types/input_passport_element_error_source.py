

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
    def read(q: dict, *args) -> "InputPassportElementErrorSourceSelfie or InputPassportElementErrorSourceFiles or InputPassportElementErrorSourceTranslationFile or InputPassportElementErrorSourceFile or InputPassportElementErrorSourceFrontSide or InputPassportElementErrorSourceDataField or InputPassportElementErrorSourceUnspecified or InputPassportElementErrorSourceTranslationFiles or InputPassportElementErrorSourceReverseSide":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElementErrorSource()
