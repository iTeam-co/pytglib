

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
    def read(q: dict, *args) -> "UpdateUnreadChatCount or UpdateNewCustomEvent or UpdateChatOnlineMemberCount or UpdateActiveNotifications or UpdateNotification or UpdateOption or UpdateAuthorizationState or UpdateFileGenerationStart or UpdateServiceNotification or UpdateLanguagePackStrings or UpdateSecretChat or UpdateChatDraftMessage or UpdateBasicGroup or UpdateMessageViews or UpdateConnectionState or UpdateScopeNotificationSettings or UpdateHavePendingNotifications or UpdateDeleteMessages or UpdateInstalledStickerSets or UpdateSavedAnimations or UpdateNewCallbackQuery or UpdateMessageContent or UpdateUserPrivacySettingRules or UpdateNewPreCheckoutQuery or UpdateNewChat or UpdateChatDefaultDisableNotification or UpdateMessageSendSucceeded or UpdateMessageEdited or UpdateChatIsMarkedAsUnread or UpdateChatOrder or UpdateChatReadOutbox or UpdateSupergroupFullInfo or UpdateChatIsSponsored or UpdateRecentStickers or UpdateCall or UpdateNewShippingQuery or UpdateNewChosenInlineResult or UpdateChatTitle or UpdateFile or UpdateFileGenerationStop or UpdateNewCustomQuery or UpdateMessageSendAcknowledged or UpdateChatNotificationSettings or UpdateChatPinnedMessage or UpdateBasicGroupFullInfo or UpdateMessageContentOpened or UpdateNotificationGroup or UpdateChatPhoto or UpdateUser or UpdateUnreadMessageCount or UpdateTrendingStickerSets or UpdateNewInlineCallbackQuery or UpdateChatReadInbox or UpdateFavoriteStickers or UpdatePoll or UpdateUserStatus or UpdateMessageMentionRead or UpdateChatIsPinned or UpdateSupergroup or UpdateNewMessage or UpdateUserChatAction or UpdateTermsOfService or UpdateUserFullInfo or UpdateNewInlineQuery or UpdateMessageSendFailed or UpdateChatUnreadMentionCount or UpdateChatLastMessage or UpdateChatReplyMarkup":
        if q.get("@type"):
            return Object.read(q)
        return Update()
