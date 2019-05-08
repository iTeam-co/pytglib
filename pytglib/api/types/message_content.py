

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
    def read(q: dict, *args) -> "MessageContactRegistered or MessageChatAddMembers or MessageText or MessageChatChangePhoto or MessageChatJoinByLink or MessageVenue or MessageGame or MessagePaymentSuccessful or MessageChatSetTtl or MessagePhoto or MessageVideo or MessageExpiredVideo or MessagePaymentSuccessfulBot or MessageCustomServiceAction or MessageChatUpgradeTo or MessageVoiceNote or MessageScreenshotTaken or MessageWebsiteConnected or MessageLocation or MessageAudio or MessageBasicGroupChatCreate or MessageContact or MessageSticker or MessageDocument or MessageExpiredPhoto or MessageChatChangeTitle or MessageChatUpgradeFrom or MessageUnsupported or MessageCall or MessageSupergroupChatCreate or MessagePassportDataSent or MessagePoll or MessagePinMessage or MessagePassportDataReceived or MessageAnimation or MessageChatDeleteMember or MessageVideoNote or MessageGameScore or MessageChatDeletePhoto or MessageInvoice":
        if q.get("@type"):
            return Object.read(q)
        return MessageContent()
