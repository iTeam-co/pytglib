

from ..utils import Object


class UserPrivacySettingAllowFindingByPhoneNumber(Object):
    """
    A privacy setting for managing whether the user can be found by their phone number. Checked only if the phone number is not known to the other user. Can be set only to "Allow contacts" or "Allow all"

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingAllowFindingByPhoneNumber``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingAllowFindingByPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingAllowFindingByPhoneNumber":
        
        return UserPrivacySettingAllowFindingByPhoneNumber()
