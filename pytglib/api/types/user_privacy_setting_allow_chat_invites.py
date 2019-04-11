

from ..utils import Object


class UserPrivacySettingAllowChatInvites(Object):
    """
    A privacy setting for managing whether the user can be invited to chats

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingAllowChatInvites``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingAllowChatInvites"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingAllowChatInvites":
        
        return UserPrivacySettingAllowChatInvites()
