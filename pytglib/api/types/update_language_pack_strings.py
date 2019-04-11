

from ..utils import Object


class UpdateLanguagePackStrings(Object):
    """
    Some language pack strings have been updated 

    Attributes:
        ID (:obj:`str`): ``UpdateLanguagePackStrings``

    Args:
        localization_target (:obj:`str`):
            Localization target to which the language pack belongs 
        language_pack_id (:obj:`str`):
            Identifier of the updated language pack 
        strings (List of :class:`telegram.api.types.languagePackString`):
            List of changed language pack strings

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateLanguagePackStrings"

    def __init__(self, localization_target, language_pack_id, strings, **kwargs):
        
        self.localization_target = localization_target  # str
        self.language_pack_id = language_pack_id  # str
        self.strings = strings  # list of languagePackString

    @staticmethod
    def read(q: dict, *args) -> "UpdateLanguagePackStrings":
        localization_target = q.get('localization_target')
        language_pack_id = q.get('language_pack_id')
        strings = [Object.read(i) for i in q.get('strings', [])]
        return UpdateLanguagePackStrings(localization_target, language_pack_id, strings)
