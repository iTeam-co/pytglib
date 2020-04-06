

from ..utils import Object


class GetChatScheduledMessages(Object):
    """
    Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id) 

    Attributes:
        ID (:obj:`str`): ``GetChatScheduledMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatScheduledMessages"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatScheduledMessages":
        chat_id = q.get('chat_id')
        return GetChatScheduledMessages(chat_id)
