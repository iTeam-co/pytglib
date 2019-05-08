

from ..utils import Object


class AddCustomServerLanguagePack(Object):
    """
    Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``AddCustomServerLanguagePack``

    Args:
        language_pack_id (:obj:`str`):
            Identifier of a language pack to be added; may be different from a name that is used in an "https://tme/setlanguage/" link

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addCustomServerLanguagePack"

    def __init__(self, language_pack_id, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str

    @staticmethod
    def read(q: dict, *args) -> "AddCustomServerLanguagePack":
        language_pack_id = q.get('language_pack_id')
        return AddCustomServerLanguagePack(language_pack_id)
