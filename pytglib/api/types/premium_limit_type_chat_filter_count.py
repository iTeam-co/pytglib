

from ..utils import Object


class PremiumLimitTypeChatFilterCount(Object):
    """
    The maximum number of chat filters

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeChatFilterCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeChatFilterCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeChatFilterCount":
        
        return PremiumLimitTypeChatFilterCount()
