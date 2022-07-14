

from ..utils import Object


class PremiumFeatureIncreasedUploadFileSize(Object):
    """
    Increased maximum upload file size

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureIncreasedUploadFileSize``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureIncreasedUploadFileSize"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureIncreasedUploadFileSize":
        
        return PremiumFeatureIncreasedUploadFileSize()
