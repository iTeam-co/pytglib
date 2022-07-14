

from ..utils import Object


class LanguagePackStringValueDeleted(Object):
    """
    A deleted language pack string, the value must be taken from the built-in English language pack

    Attributes:
        ID (:obj:`str`): ``LanguagePackStringValueDeleted``

    No parameters required.

    Returns:
        LanguagePackStringValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackStringValueDeleted"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackStringValueDeleted":
        
        return LanguagePackStringValueDeleted()
