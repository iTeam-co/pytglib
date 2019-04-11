

from ..utils import Object


class LanguagePackStringValueDeleted(Object):
    """
    A deleted language pack string, the value should be taken from the built-in english language pack

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
