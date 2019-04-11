

from ..utils import Object


class Update(Object):
    """
    Contains notifications about data changes

    No parameters required.
    """
    ID = "update"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatReplyMarkup or UpdateUser or UpdateConnectionState or UpdateNewCustomQuery or UpdateRecentStickers or UpdateChatPhoto or UpdateChatUnreadMentionCount or UpdateScopeNotificationSettings or UpdateNewCallbackQuery or UpdateMessageMentionRead or UpdateChatReadOutbox or UpdateSupergroupFullInfo or UpdateNewPreCheckoutQuery or UpdateFavoriteStickers or UpdateChatOrder or UpdateSavedAnimations or UpdateFile or UpdateChatDefaultDisableNotification or UpdateTrendingStickerSets or UpdateChatTitle or UpdateFileGenerationStart or UpdateChatReadInbox or UpdateLanguagePackStrings or UpdateUnreadChatCount or UpdateNewInlineQuery or UpdateChatDraftMessage or UpdateMessageContentOpened or UpdateMessageSendAcknowledged or UpdateMessageSendSucceeded or UpdateChatIsSponsored or UpdateChatIsMarkedAsUnread or UpdateDeleteMessages or UpdateBasicGroupFullInfo or UpdateFileGenerationStop or UpdateChatNotificationSettings or UpdateTermsOfService or UpdateUserChatAction or UpdateMessageSendFailed or UpdateMessageViews or UpdateNewChat or UpdateCall or UpdateInstalledStickerSets or UpdateUserStatus or UpdateNewChosenInlineResult or UpdateNewInlineCallbackQuery or UpdateNewMessage or UpdateNewCustomEvent or UpdateUnreadMessageCount or UpdateSupergroup or UpdateUserPrivacySettingRules or UpdateNewShippingQuery or UpdateMessageContent or UpdateChatLastMessage or UpdateOption or UpdateChatIsPinned or UpdateSecretChat or UpdateUserFullInfo or UpdateMessageEdited or UpdateAuthorizationState or UpdateBasicGroup or UpdateServiceNotification":
        if q.get("@type"):
            return Object.read(q)
        return Update()
