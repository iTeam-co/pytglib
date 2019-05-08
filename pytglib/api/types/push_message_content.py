

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
    def read(q: dict, *args) -> "PushMessageContentChatDeleteMember or PushMessageContentGame or PushMessageContentVideoNote or PushMessageContentAnimation or PushMessageContentPhoto or PushMessageContentAudio or PushMessageContentScreenshotTaken or PushMessageContentHidden or PushMessageContentGameScore or PushMessageContentChatAddMembers or PushMessageContentContactRegistered or PushMessageContentLocation or PushMessageContentMediaAlbum or PushMessageContentBasicGroupChatCreate or PushMessageContentText or PushMessageContentMessageForwards or PushMessageContentPoll or PushMessageContentInvoice or PushMessageContentChatChangePhoto or PushMessageContentSticker or PushMessageContentContact or PushMessageContentChatChangeTitle or PushMessageContentDocument or PushMessageContentVoiceNote or PushMessageContentChatJoinByLink or PushMessageContentVideo":
        if q.get("@type"):
            return Object.read(q)
        return PushMessageContent()
