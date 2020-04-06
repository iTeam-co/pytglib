

from ..utils import Object


class UserPrivacySettingShowLinkInForwardedMessages(Object):
    """
    A privacy setting for managing whether a link to the user's account is included in forwarded messages

    Attributes:
        ID (:obj:`str`): ``UserPrivacySettingShowLinkInForwardedMessages``

    No parameters required.

    Returns:
        UserPrivacySetting

    Raises:
        :class:`telegram.Error`
    """
    ID = "userPrivacySettingShowLinkInForwardedMessages"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UserPrivacySettingShowLinkInForwardedMessages":
        
        return UserPrivacySettingShowLinkInForwardedMessages()
