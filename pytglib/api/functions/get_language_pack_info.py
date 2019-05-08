

from ..utils import Object


class GetLanguagePackInfo(Object):
    """
    Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetLanguagePackInfo``

    Args:
        language_pack_id (:obj:`str`):
            Language pack identifier

    Returns:
        LanguagePackInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLanguagePackInfo"

    def __init__(self, language_pack_id, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str

    @staticmethod
    def read(q: dict, *args) -> "GetLanguagePackInfo":
        language_pack_id = q.get('language_pack_id')
        return GetLanguagePackInfo(language_pack_id)
