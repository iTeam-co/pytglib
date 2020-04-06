

from ..utils import Object


class GetAutoDownloadSettingsPresets(Object):
    """
    Returns auto-download settings presets for the currently logged in user

    Attributes:
        ID (:obj:`str`): ``GetAutoDownloadSettingsPresets``

    No parameters required.

    Returns:
        AutoDownloadSettingsPresets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAutoDownloadSettingsPresets"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetAutoDownloadSettingsPresets":
        
        return GetAutoDownloadSettingsPresets()
