

from ..utils import Object


class PremiumLimitType(Object):
    """
    Describes type of a limit, increased for Premium users

    No parameters required.
    """
    ID = "premiumLimitType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeSupergroupCount or PremiumLimitTypePinnedArchivedChatCount or PremiumLimitTypeBioLength or PremiumLimitTypeFavoriteStickerCount or PremiumLimitTypeSavedAnimationCount or PremiumLimitTypeCaptionLength or PremiumLimitTypeChatFilterChosenChatCount or PremiumLimitTypePinnedChatCount or PremiumLimitTypeCreatedPublicChatCount or PremiumLimitTypeChatFilterCount":
        if q.get("@type"):
            return Object.read(q)
        return PremiumLimitType()
