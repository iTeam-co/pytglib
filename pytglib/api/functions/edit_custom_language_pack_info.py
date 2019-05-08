

from ..utils import Object


class EditCustomLanguagePackInfo(Object):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``EditCustomLanguagePackInfo``

    Args:
        info (:class:`telegram.api.types.languagePackInfo`):
            New information about the custom local language pack

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editCustomLanguagePackInfo"

    def __init__(self, info, extra=None, **kwargs):
        self.extra = extra
        self.info = info  # LanguagePackInfo

    @staticmethod
    def read(q: dict, *args) -> "EditCustomLanguagePackInfo":
        info = Object.read(q.get('info'))
        return EditCustomLanguagePackInfo(info)
