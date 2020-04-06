

from ..utils import Object


class AutoDownloadSettingsPresets(Object):
    """
    Contains auto-download settings presets for the user

    Attributes:
        ID (:obj:`str`): ``AutoDownloadSettingsPresets``

    Args:
        low (:class:`telegram.api.types.autoDownloadSettings`):
            Preset with lowest settings; supposed to be used by default when roaming
        medium (:class:`telegram.api.types.autoDownloadSettings`):
            Preset with medium settings; supposed to be used by default when using mobile data
        high (:class:`telegram.api.types.autoDownloadSettings`):
            Preset with highest settings; supposed to be used by default when connected on Wi-Fi

    Returns:
        AutoDownloadSettingsPresets

    Raises:
        :class:`telegram.Error`
    """
    ID = "autoDownloadSettingsPresets"

    def __init__(self, low, medium, high, **kwargs):
        
        self.low = low  # AutoDownloadSettings
        self.medium = medium  # AutoDownloadSettings
        self.high = high  # AutoDownloadSettings

    @staticmethod
    def read(q: dict, *args) -> "AutoDownloadSettingsPresets":
        low = Object.read(q.get('low'))
        medium = Object.read(q.get('medium'))
        high = Object.read(q.get('high'))
        return AutoDownloadSettingsPresets(low, medium, high)
