

from ..utils import Object


class PremiumFeature(Object):
    """
    Describes a feature available to Premium users

    No parameters required.
    """
    ID = "premiumFeature"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatureIncreasedLimits or PremiumFeatureDisabledAds or PremiumFeatureAdvancedChatManagement or PremiumFeatureImprovedDownloadSpeed or PremiumFeatureAnimatedProfilePhoto or PremiumFeatureAppIcons or PremiumFeatureProfileBadge or PremiumFeatureIncreasedUploadFileSize or PremiumFeatureUniqueReactions or PremiumFeatureUniqueStickers or PremiumFeatureVoiceRecognition":
        if q.get("@type"):
            return Object.read(q)
        return PremiumFeature()
