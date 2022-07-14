

from ..utils import Object


class PremiumFeaturePromotionAnimation(Object):
    """
    Describes a promotion animation for a Premium feature 

    Attributes:
        ID (:obj:`str`): ``PremiumFeaturePromotionAnimation``

    Args:
        feature (:class:`telegram.api.types.PremiumFeature`):
            Premium feature 
        animation (:class:`telegram.api.types.animation`):
            Promotion animation for the feature

    Returns:
        PremiumFeaturePromotionAnimation

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeaturePromotionAnimation"

    def __init__(self, feature, animation, **kwargs):
        
        self.feature = feature  # PremiumFeature
        self.animation = animation  # Animation

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeaturePromotionAnimation":
        feature = Object.read(q.get('feature'))
        animation = Object.read(q.get('animation'))
        return PremiumFeaturePromotionAnimation(feature, animation)
