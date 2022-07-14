

from ..utils import Object


class PremiumLimitTypeChatFilterChosenChatCount(Object):
    """
    The maximum number of pinned and always included, or always excluded chats in a chat filter

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeChatFilterChosenChatCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeChatFilterChosenChatCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeChatFilterChosenChatCount":
        
        return PremiumLimitTypeChatFilterChosenChatCount()
