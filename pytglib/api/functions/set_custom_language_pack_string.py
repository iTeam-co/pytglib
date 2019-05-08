

from ..utils import Object


class SetCustomLanguagePackString(Object):
    """
    Adds, edits or deletes a string in a custom local language pack. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``SetCustomLanguagePackString``

    Args:
        language_pack_id (:obj:`str`):
            Identifier of a previously added custom local language pack in the current localization target 
        new_string (:class:`telegram.api.types.languagePackString`):
            New language pack string

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setCustomLanguagePackString"

    def __init__(self, language_pack_id, new_string, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str
        self.new_string = new_string  # LanguagePackString

    @staticmethod
    def read(q: dict, *args) -> "SetCustomLanguagePackString":
        language_pack_id = q.get('language_pack_id')
        new_string = Object.read(q.get('new_string'))
        return SetCustomLanguagePackString(language_pack_id, new_string)
