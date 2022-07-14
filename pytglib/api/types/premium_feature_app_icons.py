

from ..utils import Object


class PremiumFeatureAppIcons(Object):
    """
    Allowed to set a premium appllication icons

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureAppIcons``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureAppIcons"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureAppIcons":
        
        return PremiumFeatureAppIcons()
