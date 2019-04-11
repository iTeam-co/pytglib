

from ..utils import Object


class EditCustomLanguagePackInfo(Object):
    """
    Edits information about a custom language pack in the current localization target 

    Attributes:
        ID (:obj:`str`): ``EditCustomLanguagePackInfo``

    Args:
        info (:class:`telegram.api.types.languagePackInfo`):
            New information about the custom language pack

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
