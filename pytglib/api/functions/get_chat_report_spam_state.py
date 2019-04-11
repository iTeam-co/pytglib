

from ..utils import Object


class GetChatReportSpamState(Object):
    """
    Returns information on whether the current chat can be reported as spam 

    Attributes:
        ID (:obj:`str`): ``GetChatReportSpamState``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        ChatReportSpamState

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatReportSpamState"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatReportSpamState":
        chat_id = q.get('chat_id')
        return GetChatReportSpamState(chat_id)
