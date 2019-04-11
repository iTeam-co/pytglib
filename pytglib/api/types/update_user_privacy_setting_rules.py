

from ..utils import Object


class UpdateUserPrivacySettingRules(Object):
    """
    Some privacy setting rules have been changed 

    Attributes:
        ID (:obj:`str`): ``UpdateUserPrivacySettingRules``

    Args:
        setting (:class:`telegram.api.types.UserPrivacySetting`):
            The privacy setting 
        rules (:class:`telegram.api.types.userPrivacySettingRules`):
            New privacy rules

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUserPrivacySettingRules"

    def __init__(self, setting, rules, **kwargs):
        
        self.setting = setting  # UserPrivacySetting
        self.rules = rules  # UserPrivacySettingRules

    @staticmethod
    def read(q: dict, *args) -> "UpdateUserPrivacySettingRules":
        setting = Object.read(q.get('setting'))
        rules = Object.read(q.get('rules'))
        return UpdateUserPrivacySettingRules(setting, rules)
