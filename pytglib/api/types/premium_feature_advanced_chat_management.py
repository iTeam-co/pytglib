

from ..utils import Object


class PremiumFeatureAdvancedChatManagement(Object):
    """
    Ability to change position of the main chat list, archive and mute all new chats from non-contacts, and completely disable notifications about the user's contacts joined Telegram

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureAdvancedChatManagement``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureAdvancedChatManagement"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureAdvancedChatManagement":
        
        return PremiumFeatureAdvancedChatManagement()
