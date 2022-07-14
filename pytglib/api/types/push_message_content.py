

from ..utils import Object


class PushMessageContent(Object):
    """
    Contains content of a push message notification

    No parameters required.
    """
    ID = "pushMessageContent"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatDeleteMember or PushMessageContentBasicGroupChatCreate or PushMessageContentContact or PushMessageContentChatChangeTitle or PushMessageContentSticker or PushMessageContentVideoNote or PushMessageContentLocation or PushMessageContentRecurringPayment or PushMessageContentMessageForwards or PushMessageContentAudio or PushMessageContentScreenshotTaken or PushMessageContentPhoto or PushMessageContentChatJoinByLink or PushMessageContentChatChangePhoto or PushMessageContentChatSetTheme or PushMessageContentHidden or PushMessageContentChatAddMembers or PushMessageContentDocument or PushMessageContentMediaAlbum or PushMessageContentChatJoinByRequest or PushMessageContentInvoice or PushMessageContentVideo or PushMessageContentContactRegistered or PushMessageContentGame or PushMessageContentVoiceNote or PushMessageContentText or PushMessageContentGameScore or PushMessageContentAnimation or PushMessageContentPoll":
        if q.get("@type"):
            return Object.read(q)
        return PushMessageContent()
