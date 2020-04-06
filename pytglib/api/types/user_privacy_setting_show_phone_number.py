

from ..utils import Object


class UserPrivacySettingShowPhoneNumber(Object):
    """
    A privacy setting for managing whether the user's phone number is visible

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingShowPhoneNumber``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingShowPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingShowPhoneNumber":
        
        return UserPrivacySettingShowPhoneNumber()
