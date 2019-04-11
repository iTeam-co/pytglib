

from ..utils import Object


class GetChatMessageByDate(Object):
    """
    Returns the last message sent in a chat no later than the specified date 

    Attributes:
        ID (:obj:`str`): ``GetChatMessageByDate``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        date (:obj:`int`):
            Point in time (Unix timestamp) relative to which to search for messages

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatMessageByDate"

    def __init__(self, chat_id, date, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.date = date  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatMessageByDate":
        chat_id = q.get('chat_id')
        date = q.get('date')
        return GetChatMessageByDate(chat_id, date)
