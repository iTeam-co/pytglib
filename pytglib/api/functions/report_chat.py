

from ..utils import Object


class ReportChat(Object):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported

    Attributes:
        ID (:obj:`str`): ``ReportChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_ids (List of :obj:`int`):
            Identifiers of reported messages; may be empty to report the whole chat 
        reason (:class:`telegram.api.types.ChatReportReason`):
            The reason for reporting the chat 
        text (:obj:`str`):
            Additional report details; 0-1024 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reportChat"

    def __init__(self, chat_id, message_ids, reason, text, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int
        self.reason = reason  # ChatReportReason
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "ReportChat":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        reason = Object.read(q.get('reason'))
        text = q.get('text')
        return ReportChat(chat_id, message_ids, reason, text)
