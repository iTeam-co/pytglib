

from ..utils import Object


class PremiumLimitTypeCreatedPublicChatCount(Object):
    """
    The maximum number of created public chats

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeCreatedPublicChatCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeCreatedPublicChatCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeCreatedPublicChatCount":
        
        return PremiumLimitTypeCreatedPublicChatCount()
