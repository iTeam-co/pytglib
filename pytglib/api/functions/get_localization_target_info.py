

from ..utils import Object


class GetLocalizationTargetInfo(Object):
    """
    Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetLocalizationTargetInfo``

    Args:
        only_local (:obj:`bool`):
            If true, returns only locally available information without sending network requests

    Returns:
        LocalizationTargetInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLocalizationTargetInfo"

    def __init__(self, only_local, extra=None, **kwargs):
        self.extra = extra
        self.only_local = only_local  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetLocalizationTargetInfo":
        only_local = q.get('only_local')
        return GetLocalizationTargetInfo(only_local)
