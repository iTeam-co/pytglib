

from ..utils import Object


class PremiumLimitTypePinnedChatCount(Object):
    """
    The maximum number of pinned chats in the main chat list

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypePinnedChatCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypePinnedChatCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypePinnedChatCount":
        
        return PremiumLimitTypePinnedChatCount()
