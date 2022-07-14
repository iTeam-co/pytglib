

from ..utils import Object


class PremiumLimitTypeSavedAnimationCount(Object):
    """
    The maximum number of saved animations

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeSavedAnimationCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeSavedAnimationCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeSavedAnimationCount":
        
        return PremiumLimitTypeSavedAnimationCount()
