

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
    def read(q: dict, *args) -> "MessagePinMessage or MessageContact or MessageChatSetTtl or MessageLocation or MessageVideo or MessageAnimation or MessagePhoto or MessageChatChangeTitle or MessagePaymentSuccessfulBot or MessageGame or MessageBasicGroupChatCreate or MessageInvoice or MessagePaymentSuccessful or MessageChatDeletePhoto or MessageChatJoinByLink or MessageChatChangePhoto or MessageSupergroupChatCreate or MessageScreenshotTaken or MessagePassportDataSent or MessageChatUpgradeTo or MessageWebsiteConnected or MessageCustomServiceAction or MessageContactRegistered or MessageText or MessagePassportDataReceived or MessageGameScore or MessageVenue or MessageDocument or MessageExpiredVideo or MessageChatAddMembers or MessageCall or MessageAudio or MessageVideoNote or MessageExpiredPhoto or MessageChatDeleteMember or MessageChatUpgradeFrom or MessageUnsupported or MessageSticker or MessageVoiceNote":
        if q.get("@type"):
            return Object.read(q)
        return MessageContent()
