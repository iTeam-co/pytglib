

from ..utils import Object


class SetUserPrivacySettingRules(Object):
    """
    Changes user privacy settings 

    Attributes:
        ID (:obj:`str`): ``SetUserPrivacySettingRules``

    Args:
        setting (:class:`telegram.api.types.UserPrivacySetting`):
            The privacy setting 
        rules (:class:`telegram.api.types.userPrivacySettingRules`):
            The new privacy rules

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setUserPrivacySettingRules"

    def __init__(self, setting, rules, extra=None, **kwargs):
        self.extra = extra
        self.setting = setting  # UserPrivacySetting
        self.rules = rules  # UserPrivacySettingRules

    @staticmethod
    def read(q: dict, *args) -> "SetUserPrivacySettingRules":
        setting = Object.read(q.get('setting'))
        rules = Object.read(q.get('rules'))
        return SetUserPrivacySettingRules(setting, rules)
