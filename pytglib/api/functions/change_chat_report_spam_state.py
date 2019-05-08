

from ..utils import Object


class ChangeChatReportSpamState(Object):
    """
    Reports to the server whether a chat is a spam chat or not. Can be used only if ChatReportSpamState.can_report_spam is true. After this request, ChatReportSpamState.can_report_spam becomes false forever 

    Attributes:
        ID (:obj:`str`): ``ChangeChatReportSpamState``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_spam_chat (:obj:`bool`):
            If true, the chat will be reported as spam; otherwise it will be marked as not spam

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "changeChatReportSpamState"

    def __init__(self, chat_id, is_spam_chat, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.is_spam_chat = is_spam_chat  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChangeChatReportSpamState":
        chat_id = q.get('chat_id')
        is_spam_chat = q.get('is_spam_chat')
        return ChangeChatReportSpamState(chat_id, is_spam_chat)
