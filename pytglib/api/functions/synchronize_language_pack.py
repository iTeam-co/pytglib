

from ..utils import Object


class SynchronizeLanguagePack(Object):
    """
    Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method doesn't need to be called explicitly for the current used/base language packs. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``SynchronizeLanguagePack``

    Args:
        language_pack_id (:obj:`str`):
            Language pack identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "synchronizeLanguagePack"

    def __init__(self, language_pack_id, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str

    @staticmethod
    def read(q: dict, *args) -> "SynchronizeLanguagePack":
        language_pack_id = q.get('language_pack_id')
        return SynchronizeLanguagePack(language_pack_id)
