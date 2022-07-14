

from ..utils import Object


class PremiumFeatureAnimatedProfilePhoto(Object):
    """
    Profile photo animation on message and chat screens

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureAnimatedProfilePhoto``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureAnimatedProfilePhoto"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureAnimatedProfilePhoto":
        
        return PremiumFeatureAnimatedProfilePhoto()
