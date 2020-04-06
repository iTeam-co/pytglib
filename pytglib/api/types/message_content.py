

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
    def read(q: dict, *args) -> "MessageDocument or MessageVoiceNote or MessagePaymentSuccessfulBot or MessageContactRegistered or MessageVenue or MessageChatChangePhoto or MessageWebsiteConnected or MessageSticker or MessageChatUpgradeTo or MessageContact or MessageCustomServiceAction or MessagePoll or MessageExpiredPhoto or MessageChatSetTtl or MessageVideo or MessageChatJoinByLink or MessageUnsupported or MessageVideoNote or MessagePhoto or MessageExpiredVideo or MessagePinMessage or MessagePaymentSuccessful or MessageSupergroupChatCreate or MessageText or MessageDice or MessageChatDeleteMember or MessageGame or MessageInvoice or MessageChatUpgradeFrom or MessagePassportDataReceived or MessageLocation or MessagePassportDataSent or MessageGameScore or MessageScreenshotTaken or MessageCall or MessageChatAddMembers or MessageAudio or MessageBasicGroupChatCreate or MessageChatChangeTitle or MessageAnimation or MessageChatDeletePhoto":
        if q.get("@type"):
            return Object.read(q)
        return MessageContent()
