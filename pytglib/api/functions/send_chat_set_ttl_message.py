

from ..utils import Object


class SendChatSetTtlMessage(Object):
    """
    Changes the current TTL setting (sets a new self-destruct timer) in a secret chat and sends the corresponding message 

    Attributes:
        ID (:obj:`str`): ``SendChatSetTtlMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        ttl (:obj:`int`):
            New TTL value, in seconds

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendChatSetTtlMessage"

    def __init__(self, chat_id, ttl, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.ttl = ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "SendChatSetTtlMessage":
        chat_id = q.get('chat_id')
        ttl = q.get('ttl')
        return SendChatSetTtlMessage(chat_id, ttl)
