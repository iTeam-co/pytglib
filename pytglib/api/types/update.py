

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
    def read(q: dict, *args) -> "UpdateChatOrder or UpdateNotificationGroup or UpdateNewMessage or UpdateChatPinnedMessage or UpdateTermsOfService or UpdateUserStatus or UpdateUsersNearby or UpdateUserPrivacySettingRules or UpdateFile or UpdateMessageSendAcknowledged or UpdateSecretChat or UpdateNewInlineQuery or UpdateLanguagePackStrings or UpdateMessageSendFailed or UpdateUserChatAction or UpdateUser or UpdateChatIsMarkedAsUnread or UpdateChatReadInbox or UpdateChatPhoto or UpdateChatIsPinned or UpdateHavePendingNotifications or UpdateBasicGroup or UpdateMessageViews or UpdatePollAnswer or UpdateSupergroup or UpdateNotification or UpdateMessageLiveLocationViewed or UpdateRecentStickers or UpdateNewPreCheckoutQuery or UpdateMessageSendSucceeded or UpdateChatDraftMessage or UpdateChatDefaultDisableNotification or UpdateUnreadChatCount or UpdateNewChosenInlineResult or UpdateUnreadMessageCount or UpdateChatHasScheduledMessages or UpdateCall or UpdateNewInlineCallbackQuery or UpdateMessageContentOpened or UpdateChatTitle or UpdateSavedAnimations or UpdateChatNotificationSettings or UpdateNewCustomEvent or UpdateBasicGroupFullInfo or UpdateMessageContent or UpdateAuthorizationState or UpdateNewShippingQuery or UpdateConnectionState or UpdateChatOnlineMemberCount or UpdateChatActionBar or UpdateSupergroupFullInfo or UpdateTrendingStickerSets or UpdateFavoriteStickers or UpdateSelectedBackground or UpdateChatIsSponsored or UpdateNewCallbackQuery or UpdateChatChatList or UpdateChatPermissions or UpdateNewChat or UpdateChatReadOutbox or UpdateActiveNotifications or UpdatePoll or UpdateMessageMentionRead or UpdateMessageEdited or UpdateScopeNotificationSettings or UpdateChatLastMessage or UpdateUserFullInfo or UpdateChatReplyMarkup or UpdateChatUnreadMentionCount or UpdateServiceNotification or UpdateFileGenerationStart or UpdateNewCustomQuery or UpdateFileGenerationStop or UpdateInstalledStickerSets or UpdateDeleteMessages or UpdateOption":
        if q.get("@type"):
            return Object.read(q)
        return Update()
