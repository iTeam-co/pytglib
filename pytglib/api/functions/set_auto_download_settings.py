

from ..utils import Object


class SetAutoDownloadSettings(Object):
    """
    Sets auto-download settings 

    Attributes:
        ID (:obj:`str`): ``SetAutoDownloadSettings``

    Args:
        settings (:class:`telegram.api.types.autoDownloadSettings`):
            New user auto-download settings 
        type (:class:`telegram.api.types.NetworkType`):
            Type of the network for which the new settings are applied

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setAutoDownloadSettings"

    def __init__(self, settings, type, extra=None, **kwargs):
        self.extra = extra
        self.settings = settings  # AutoDownloadSettings
        self.type = type  # NetworkType

    @staticmethod
    def read(q: dict, *args) -> "SetAutoDownloadSettings":
        settings = Object.read(q.get('settings'))
        type = Object.read(q.get('type'))
        return SetAutoDownloadSettings(settings, type)
