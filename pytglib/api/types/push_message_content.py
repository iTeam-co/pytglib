

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
    def read(q: dict, *args) -> "PushMessageContentVoiceNote or PushMessageContentHidden or PushMessageContentContact or PushMessageContentAudio or PushMessageContentChatDeleteMember or PushMessageContentVideoNote or PushMessageContentContactRegistered or PushMessageContentScreenshotTaken or PushMessageContentMediaAlbum or PushMessageContentChatChangeTitle or PushMessageContentAnimation or PushMessageContentChatJoinByLink or PushMessageContentPhoto or PushMessageContentChatChangePhoto or PushMessageContentSticker or PushMessageContentInvoice or PushMessageContentGame or PushMessageContentGameScore or PushMessageContentVideo or PushMessageContentLocation or PushMessageContentDocument or PushMessageContentText or PushMessageContentMessageForwards or PushMessageContentBasicGroupChatCreate or PushMessageContentPoll or PushMessageContentChatAddMembers":
        if q.get("@type"):
            return Object.read(q)
        return PushMessageContent()
