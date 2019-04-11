

from ..utils import Object


class LanguagePackStrings(Object):
    """
    Contains a list of language pack strings 

    Attributes:
        ID (:obj:`str`): ``LanguagePackStrings``

    Args:
        strings (List of :class:`telegram.api.types.languagePackString`):
            A list of language pack strings

    Returns:
        LanguagePackStrings

    Raises:
        :class:`telegram.Error`
    """
    ID = "languagePackStrings"

    def __init__(self, strings, **kwargs):
        
        self.strings = strings  # list of languagePackString

    @staticmethod
    def read(q: dict, *args) -> "LanguagePackStrings":
        strings = [Object.read(i) for i in q.get('strings', [])]
        return LanguagePackStrings(strings)
