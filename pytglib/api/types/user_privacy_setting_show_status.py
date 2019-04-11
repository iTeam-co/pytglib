

from ..utils import Object


class UserPrivacySettingShowStatus(Object):
    """
    A privacy setting for managing whether the user's online status is visible

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingShowStatus``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingShowStatus"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingShowStatus":
        
        return UserPrivacySettingShowStatus()
