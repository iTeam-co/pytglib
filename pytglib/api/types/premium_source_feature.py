

from ..utils import Object


class PremiumSourceFeature(Object):
    """
    A user tried to use a Premium feature 

    Attributes:
        ID (:obj:`str`): ``PremiumSourceFeature``

    Args:
        feature (:class:`telegram.api.types.PremiumFeature`):
            The used feature

    Returns:
        PremiumSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumSourceFeature"

    def __init__(self, feature, **kwargs):
        
        self.feature = feature  # PremiumFeature

    @staticmethod
    def read(q: dict, *args) -> "PremiumSourceFeature":
        feature = Object.read(q.get('feature'))
        return PremiumSourceFeature(feature)
