

from ..utils import Object


class UserPrivacySettingAllowCalls(Object):
    """
    A privacy setting for managing whether the user can be called

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingAllowCalls``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingAllowCalls"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingAllowCalls":
        
        return UserPrivacySettingAllowCalls()
