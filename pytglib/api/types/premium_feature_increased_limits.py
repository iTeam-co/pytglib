

from ..utils import Object


class PremiumFeatureIncreasedLimits(Object):
    """
    Increased limits

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureIncreasedLimits``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureIncreasedLimits"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureIncreasedLimits":
        
        return PremiumFeatureIncreasedLimits()
