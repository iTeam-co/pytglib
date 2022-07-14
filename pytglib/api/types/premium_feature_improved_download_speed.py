

from ..utils import Object


class PremiumFeatureImprovedDownloadSpeed(Object):
    """
    Improved download speed

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureImprovedDownloadSpeed``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureImprovedDownloadSpeed"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureImprovedDownloadSpeed":
        
        return PremiumFeatureImprovedDownloadSpeed()
