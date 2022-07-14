

from ..utils import Object


class PremiumFeatureVoiceRecognition(Object):
    """
    The ability to convert voice notes to text

    Attributes:
        ID (:obj:`str`): ``PremiumFeatureVoiceRecognition``

    No parameters required.

    Returns:
        PremiumFeature

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatureVoiceRecognition"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureVoiceRecognition":
        
        return PremiumFeatureVoiceRecognition()
