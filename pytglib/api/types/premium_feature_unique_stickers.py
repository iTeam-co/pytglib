

from ..utils import Object


class PremiumFeatureUniqueStickers(Object):
    """
    Allowed to use premium stickers with unique effects

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureUniqueStickers``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureUniqueStickers"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureUniqueStickers":
        
        return PremiumFeatureUniqueStickers()
