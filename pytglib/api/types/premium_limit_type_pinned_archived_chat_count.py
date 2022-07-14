

from ..utils import Object


class PremiumLimitTypePinnedArchivedChatCount(Object):
    """
    The maximum number of pinned chats in the archive chat list

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypePinnedArchivedChatCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypePinnedArchivedChatCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypePinnedArchivedChatCount":
        
        return PremiumLimitTypePinnedArchivedChatCount()
