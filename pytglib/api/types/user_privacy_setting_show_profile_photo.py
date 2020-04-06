

from ..utils import Object


class UserPrivacySettingShowProfilePhoto(Object):
    """
    A privacy setting for managing whether the user's profile photo is visible

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingShowProfilePhoto``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingShowProfilePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingShowProfilePhoto":
        
        return UserPrivacySettingShowProfilePhoto()
