

from ..utils import Object


class UpdateMessageContentOpened(Object):
    """
    The message content was opened. Updates voice note messages to "listened", video note messages to "viewed" and starts the TTL timer for self-destructing messages 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageContentOpened``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageContentOpened"

    def __init__(self, chat_id, message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageContentOpened":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return UpdateMessageContentOpened(chat_id, message_id)
