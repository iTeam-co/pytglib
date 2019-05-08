

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
    def read(q: dict, *args) -> "MessageVideo or MessageCustomServiceAction or MessageAnimation or MessageContactRegistered or MessageVoiceNote or MessageContact or MessageAudio or MessageChatChangeTitle or MessageSupergroupChatCreate or MessagePinMessage or MessageUnsupported or MessageChatUpgradeTo or MessageInvoice or MessageExpiredVideo or MessageBasicGroupChatCreate or MessageChatJoinByLink or MessageExpiredPhoto or MessageCall or MessagePaymentSuccessfulBot or MessageScreenshotTaken or MessageChatSetTtl or MessageGame or MessageDocument or MessageChatAddMembers or MessageLocation or MessageVideoNote or MessagePassportDataReceived or MessageVenue or MessageChatUpgradeFrom or MessageChatDeletePhoto or MessageWebsiteConnected or MessageChatChangePhoto or MessagePaymentSuccessful or MessageSticker or MessagePoll or MessageGameScore or MessageChatDeleteMember or MessagePassportDataSent or MessagePhoto or MessageText":
        if q.get("@type"):
            return Object.read(q)
        return MessageContent()
