

from ..utils import Object


class PremiumFeatureProfileBadge(Object):
    """
    A badge in the user's profile

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureProfileBadge``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureProfileBadge"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureProfileBadge":
        
        return PremiumFeatureProfileBadge()
