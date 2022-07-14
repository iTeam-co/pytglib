

from ..utils import Object


class ChatEventMessageTtlChanged(Object):
    """
    The message TTL was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventMessageTtlChanged``

    Args:
        old_message_ttl (:obj:`int`):
            Previous value of message_ttl 
        new_message_ttl (:obj:`int`):
            New value of message_ttl

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessageTtlChanged"

    def __init__(self, old_message_ttl, new_message_ttl, **kwargs):
        
        self.old_message_ttl = old_message_ttl  # int
        self.new_message_ttl = new_message_ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessageTtlChanged":
        old_message_ttl = q.get('old_message_ttl')
        new_message_ttl = q.get('new_message_ttl')
        return ChatEventMessageTtlChanged(old_message_ttl, new_message_ttl)
