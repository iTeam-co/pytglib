

from ..utils import Object


class InternalLinkType(Object):
    """
    Describes an internal https://t.me or tg: link, which must be processed by the application in a special way

    No parameters required.
    """
    ID = "internalLinkType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeBackground or InternalLinkTypeAttachmentMenuBot or InternalLinkTypeActiveSessions or InternalLinkTypeTheme or InternalLinkTypeVideoChat or InternalLinkTypeBotAddToChannel or InternalLinkTypeLanguagePack or InternalLinkTypeMessage or InternalLinkTypeUserPhoneNumber or InternalLinkTypeThemeSettings or InternalLinkTypeInvoice or InternalLinkTypeQrCodeAuthentication or InternalLinkTypeAuthenticationCode or InternalLinkTypePremiumFeatures or InternalLinkTypeProxy or InternalLinkTypeMessageDraft or InternalLinkTypePassportDataRequest or InternalLinkTypeSettings or InternalLinkTypeUnknownDeepLink or InternalLinkTypeChatInvite or InternalLinkTypeBotStart or InternalLinkTypeFilterSettings or InternalLinkTypeUnsupportedProxy or InternalLinkTypePublicChat or InternalLinkTypeBotStartInGroup or InternalLinkTypeStickerSet or InternalLinkTypeGame or InternalLinkTypePhoneNumberConfirmation or InternalLinkTypeLanguageSettings or InternalLinkTypePrivacyAndSecuritySettings or InternalLinkTypeChangePhoneNumber":
        if q.get("@type"):
            return Object.read(q)
        return InternalLinkType()
