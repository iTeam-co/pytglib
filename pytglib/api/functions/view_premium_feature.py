

from ..utils import Object


class ViewPremiumFeature(Object):
    """
    Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen 

    Attributes:
        ID (:obj:`str`): ``ViewPremiumFeature``

    Args:
        feature (:class:`telegram.api.types.PremiumFeature`):
            The viewed premium feature

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "viewPremiumFeature"

    def __init__(self, feature, extra=None, **kwargs):
        self.extra = extra
        self.feature = feature  # PremiumFeature

    @staticmethod
    def read(q: dict, *args) -> "ViewPremiumFeature":
        feature = Object.read(q.get('feature'))
        return ViewPremiumFeature(feature)
