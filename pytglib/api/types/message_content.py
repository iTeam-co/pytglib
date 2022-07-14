

from ..utils import Object


class MessageContent(Object):
    """
    Contains the content of a message

    No parameters required.
    """
    ID = "messageContent"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageChatUpgradeTo or MessageWebAppDataReceived or MessageDice or MessageVideoChatScheduled or MessageGameScore or MessageContactRegistered or MessageChatJoinByLink or MessageChatSetTtl or MessagePaymentSuccessfulBot or MessageChatUpgradeFrom or MessageProximityAlertTriggered or MessageVideo or MessagePhoto or MessageText or MessagePinMessage or MessageSupergroupChatCreate or MessageChatSetTheme or MessageBasicGroupChatCreate or MessageGame or MessageChatChangeTitle or MessageLocation or MessagePassportDataReceived or MessageExpiredPhoto or MessageAnimatedEmoji or MessageVenue or MessageVideoNote or MessageChatAddMembers or MessageChatChangePhoto or MessageWebAppDataSent or MessageScreenshotTaken or MessageCall or MessageVoiceNote or MessagePaymentSuccessful or MessageDocument or MessageSticker or MessageVideoChatStarted or MessageInviteVideoChatParticipants or MessagePassportDataSent or MessageContact or MessageInvoice or MessageWebsiteConnected or MessageChatDeletePhoto or MessageAudio or MessageCustomServiceAction or MessageUnsupported or MessageVideoChatEnded or MessagePoll or MessageAnimation or MessageChatJoinByRequest or MessageChatDeleteMember or MessageExpiredVideo":
        if q.get("@type"):
            return Object.read(q)
        return MessageContent()
