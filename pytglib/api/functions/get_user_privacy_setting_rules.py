

from ..utils import Object


class GetUserPrivacySettingRules(Object):
    """
    Returns the current privacy settings 

    Attributes:
        ID (:obj:`str`): ``GetUserPrivacySettingRules``

    Args:
        setting (:class:`telegram.api.types.UserPrivacySetting`):
            The privacy setting

    Returns:
        UserPrivacySettingRules

    Raises:
        :class:`telegram.Error`
    """
    ID = "getUserPrivacySettingRules"

    def __init__(self, setting, extra=None, **kwargs):
        self.extra = extra
        self.setting = setting  # UserPrivacySetting

    @staticmethod
    def read(q: dict, *args) -> "GetUserPrivacySettingRules":
        setting = Object.read(q.get('setting'))
        return GetUserPrivacySettingRules(setting)
