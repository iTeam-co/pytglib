

from ..utils import Object


class ReportChat(Object):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if this is a private chats with a bot, a private chat with a user sharing their location, a supergroup, or a channel, since other chats can't be checked by moderators 

    Attributes:
        ID (:obj:`str`): ``ReportChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        reason (:class:`telegram.api.types.ChatReportReason`):
            The reason for reporting the chat 
        message_ids (List of :obj:`int`):
            Identifiers of reported messages, if any

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reportChat"

    def __init__(self, chat_id, reason, message_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.reason = reason  # ChatReportReason
        self.message_ids = message_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ReportChat":
        chat_id = q.get('chat_id')
        reason = Object.read(q.get('reason'))
        message_ids = q.get('message_ids')
        return ReportChat(chat_id, reason, message_ids)
