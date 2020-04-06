

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
    def read(q: dict, *args) -> "PushMessageContentContact or PushMessageContentPoll or PushMessageContentAudio or PushMessageContentChatChangeTitle or PushMessageContentMessageForwards or PushMessageContentBasicGroupChatCreate or PushMessageContentLocation or PushMessageContentChatJoinByLink or PushMessageContentSticker or PushMessageContentInvoice or PushMessageContentVideoNote or PushMessageContentChatChangePhoto or PushMessageContentText or PushMessageContentChatDeleteMember or PushMessageContentHidden or PushMessageContentMediaAlbum or PushMessageContentScreenshotTaken or PushMessageContentPhoto or PushMessageContentContactRegistered or PushMessageContentChatAddMembers or PushMessageContentVoiceNote or PushMessageContentGameScore or PushMessageContentVideo or PushMessageContentAnimation or PushMessageContentGame or PushMessageContentDocument":
        if q.get("@type"):
            return Object.read(q)
        return PushMessageContent()
