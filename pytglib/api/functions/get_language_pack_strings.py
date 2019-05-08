

from ..utils import Object


class GetLanguagePackStrings(Object):
    """
    Returns strings from a language pack in the current localization target by their keys. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetLanguagePackStrings``

    Args:
        language_pack_id (:obj:`str`):
            Language pack identifier of the strings to be returned 
        keys (List of :obj:`str`):
            Language pack keys of the strings to be returned; leave empty to request all available strings

    Returns:
        LanguagePackStrings

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLanguagePackStrings"

    def __init__(self, language_pack_id, keys, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str
        self.keys = keys  # list of str

    @staticmethod
    def read(q: dict, *args) -> "GetLanguagePackStrings":
        language_pack_id = q.get('language_pack_id')
        keys = q.get('keys')
        return GetLanguagePackStrings(language_pack_id, keys)
