

from ..utils import Object


class ReportChatPhoto(Object):
    """
    Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported

    Attributes:
        ID (:obj:`str`): ``ReportChatPhoto``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        file_id (:obj:`int`):
            Identifier of the photo to reportOnly full photos from chatPhoto can be reported 
        reason (:class:`telegram.api.types.ChatReportReason`):
            The reason for reporting the chat photo 
        text (:obj:`str`):
            Additional report details; 0-1024 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reportChatPhoto"

    def __init__(self, chat_id, file_id, reason, text, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.file_id = file_id  # int
        self.reason = reason  # ChatReportReason
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "ReportChatPhoto":
        chat_id = q.get('chat_id')
        file_id = q.get('file_id')
        reason = Object.read(q.get('reason'))
        text = q.get('text')
        return ReportChatPhoto(chat_id, file_id, reason, text)
