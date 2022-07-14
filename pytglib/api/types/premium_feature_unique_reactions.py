

from ..utils import Object


class PremiumFeatureUniqueReactions(Object):
    """
    Allowed to use more reactions

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureUniqueReactions``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureUniqueReactions"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureUniqueReactions":
        
        return PremiumFeatureUniqueReactions()
