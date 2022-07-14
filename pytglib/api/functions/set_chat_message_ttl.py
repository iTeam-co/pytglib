

from ..utils import Object


class SetChatMessageTtl(Object):
    """
    Changes the message TTL in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channelsMessage TTL can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).

    Attributes:
        ID (:obj:`str`): ``SetChatMessageTtl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        ttl (:obj:`int`):
            New TTL value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatMessageTtl"

    def __init__(self, chat_id, ttl, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.ttl = ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "SetChatMessageTtl":
        chat_id = q.get('chat_id')
        ttl = q.get('ttl')
        return SetChatMessageTtl(chat_id, ttl)
