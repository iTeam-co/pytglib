

from ..utils import Object


class LanguagePackStringValue(Object):
    """
    Represents the value of a string in a language pack

    No parameters required.
    """
    ID = "languagePackStringValue"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackStringValueDeleted or LanguagePackStringValuePluralized or LanguagePackStringValueOrdinary":
        if q.get("@type"):
            return Object.read(q)
        return LanguagePackStringValue()
