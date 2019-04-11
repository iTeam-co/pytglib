

from ..utils import Object


class DeleteLanguagePack(Object):
    """
    Deletes all information about a language pack in the current localization target. The language pack that is currently in use can't be deleted 

    Attributes:
        ID (:obj:`str`): ``DeleteLanguagePack``

    Args:
        language_pack_id (:obj:`str`):
            Identifier of the language pack to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteLanguagePack"

    def __init__(self, language_pack_id, extra=None, **kwargs):
        self.extra = extra
        self.language_pack_id = language_pack_id  # str

    @staticmethod
    def read(q: dict, *args) -> "DeleteLanguagePack":
        language_pack_id = q.get('language_pack_id')
        return DeleteLanguagePack(language_pack_id)
