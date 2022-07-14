

from ..utils import Object


class MessageChatSetTtl(Object):
    """
    The TTL (Time To Live) setting for messages in the chat has been changed 

    Attributes:
        ID (:obj:`str`): ``MessageChatSetTtl``

    Args:
        ttl (:obj:`int`):
            New message TTL

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatSetTtl"

    def __init__(self, ttl, **kwargs):
        
        self.ttl = ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageChatSetTtl":
        ttl = q.get('ttl')
        return MessageChatSetTtl(ttl)
