

from ..utils import Object


class PremiumFeatureDisabledAds(Object):
    """
    Disabled ads

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureDisabledAds``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureDisabledAds"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureDisabledAds":
        
        return PremiumFeatureDisabledAds()
