

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
    def read(q: dict, *args) -> "UpdateBasicGroupFullInfo or UpdateGroupCallParticipant or UpdateChatAvailableReactions or UpdateNewMessage or UpdateChatMember or UpdateWebAppMessageSent or UpdateLanguagePackStrings or UpdateMessageContent or UpdateReactions or UpdateChatReplyMarkup or UpdateDiceEmojis or UpdateChatUnreadReactionCount or UpdateSuggestedActions or UpdateFileGenerationStop or UpdateUsersNearby or UpdateSupergroupFullInfo or UpdateNotificationGroup or UpdateGroupCall or UpdateNewChat or UpdateChatLastMessage or UpdateAnimationSearchParameters or UpdateChatUnreadMentionCount or UpdateMessageContentOpened or UpdateChatReadInbox or UpdateUnreadChatCount or UpdateFileGenerationStart or UpdateChatPhoto or UpdateSelectedBackground or UpdateScopeNotificationSettings or UpdateChatOnlineMemberCount or UpdateNewCallSignalingData or UpdateNewChosenInlineResult or UpdateChatVideoChat or UpdateMessageSendAcknowledged or UpdateUserPrivacySettingRules or UpdateNewCallbackQuery or UpdateNewPreCheckoutQuery or UpdateChatHasProtectedContent or UpdateHavePendingNotifications or UpdateChatIsMarkedAsUnread or UpdateBasicGroup or UpdateFileRemovedFromDownloads or UpdateServiceNotification or UpdateInstalledStickerSets or UpdateTrendingStickerSets or UpdateChatMessageTtl or UpdateUserFullInfo or UpdateSavedNotificationSounds or UpdateNewShippingQuery or UpdateFavoriteStickers or UpdateFileDownloads or UpdateChatIsBlocked or UpdateDeleteMessages or UpdateMessageUnreadReactions or UpdateChatDefaultDisableNotification or UpdateMessageInteractionInfo or UpdateNewInlineCallbackQuery or UpdateSecretChat or UpdateFileDownload or UpdateMessageEdited or UpdateNewInlineQuery or UpdateUnreadMessageCount or UpdateChatTheme or UpdateMessageLiveLocationViewed or UpdateChatPosition or UpdateNewCustomQuery or UpdatePollAnswer or UpdateAttachmentMenuBots or UpdateRecentStickers or UpdateMessageSendFailed or UpdateMessageIsPinned or UpdateStickerSet or UpdateFileAddedToDownloads or UpdateTermsOfService or UpdateConnectionState or UpdateOption or UpdateChatMessageSender or UpdateChatHasScheduledMessages or UpdateChatPendingJoinRequests or UpdateAuthorizationState or UpdateMessageMentionRead or UpdateChatAction or UpdateUser or UpdateChatActionBar or UpdateNewCustomEvent or UpdateChatThemes or UpdateNewChatJoinRequest or UpdateChatPermissions or UpdatePoll or UpdateActiveNotifications or UpdateChatFilters or UpdateMessageSendSucceeded or UpdateCall or UpdateSavedAnimations or UpdateChatTitle or UpdateSupergroup or UpdateChatNotificationSettings or UpdateAnimatedEmojiMessageClicked or UpdateNotification or UpdateUserStatus or UpdateChatReadOutbox or UpdateFile or UpdateChatDraftMessage":
        if q.get("@type"):
            return Object.read(q)
        return Update()
