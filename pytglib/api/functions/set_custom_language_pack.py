

from ..utils import Object


class SetCustomLanguagePack(Object):
    """
    Adds or changes a custom local language pack to the current localization target 

    Attributes:
        ID (:obj:`str`): ``SetCustomLanguagePack``

    Args:
        info (:class:`telegram.api.types.languagePackInfo`):
            Information about the language packLanguage pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 charactersCan be called before authorization 
        strings (List of :class:`telegram.api.types.languagePackString`):
            Strings of the new language pack

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setCustomLanguagePack"

    def __init__(self, info, strings, extra=None, **kwargs):
        self.extra = extra
        self.info = info  # LanguagePackInfo
        self.strings = strings  # list of languagePackString

    @staticmethod
    def read(q: dict, *args) -> "SetCustomLanguagePack":
        info = Object.read(q.get('info'))
        strings = [Object.read(i) for i in q.get('strings', [])]
        return SetCustomLanguagePack(info, strings)
