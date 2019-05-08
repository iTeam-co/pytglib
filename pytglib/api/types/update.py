

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
    def read(q: dict, *args) -> "UpdateNotificationGroup or UpdateSupergroup or UpdateUserPrivacySettingRules or UpdateChatIsMarkedAsUnread or UpdateNewInlineQuery or UpdateTermsOfService or UpdateHavePendingNotifications or UpdateChatNotificationSettings or UpdateUserStatus or UpdateNewChat or UpdatePoll or UpdateNewCustomQuery or UpdateBasicGroup or UpdateSupergroupFullInfo or UpdateNewShippingQuery or UpdateChatReadInbox or UpdateTrendingStickerSets or UpdateFavoriteStickers or UpdateRecentStickers or UpdateChatOnlineMemberCount or UpdateActiveNotifications or UpdateUserChatAction or UpdateNewCallbackQuery or UpdateOption or UpdateAuthorizationState or UpdateMessageMentionRead or UpdateFile or UpdateChatLastMessage or UpdateBasicGroupFullInfo or UpdateScopeNotificationSettings or UpdateNewMessage or UpdateMessageEdited or UpdateMessageSendFailed or UpdateChatTitle or UpdateUserFullInfo or UpdateFileGenerationStop or UpdateChatOrder or UpdateChatDefaultDisableNotification or UpdateChatReplyMarkup or UpdateNotification or UpdateSecretChat or UpdateServiceNotification or UpdateInstalledStickerSets or UpdateNewInlineCallbackQuery or UpdateMessageViews or UpdateUnreadMessageCount or UpdateChatIsSponsored or UpdateMessageContent or UpdateChatIsPinned or UpdateSavedAnimations or UpdateNewCustomEvent or UpdateCall or UpdateChatDraftMessage or UpdateLanguagePackStrings or UpdateChatReadOutbox or UpdateChatPinnedMessage or UpdateConnectionState or UpdateUser or UpdateMessageSendSucceeded or UpdateDeleteMessages or UpdateChatPhoto or UpdateNewChosenInlineResult or UpdateMessageSendAcknowledged or UpdateMessageContentOpened or UpdateUnreadChatCount or UpdateChatUnreadMentionCount or UpdateNewPreCheckoutQuery or UpdateFileGenerationStart":
        if q.get("@type"):
            return Object.read(q)
        return Update()
