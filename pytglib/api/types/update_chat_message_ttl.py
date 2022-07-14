

from ..utils import Object


class UpdateChatMessageTtl(Object):
    """
    The message Time To Live setting for a chat was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatMessageTtl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_ttl (:obj:`int`):
            New value of message_ttl

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatMessageTtl"

    def __init__(self, chat_id, message_ttl, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_ttl = message_ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatMessageTtl":
        chat_id = q.get('chat_id')
        message_ttl = q.get('message_ttl')
        return UpdateChatMessageTtl(chat_id, message_ttl)
