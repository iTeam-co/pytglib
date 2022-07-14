

from ..utils import Object


class ToggleMessageSenderIsBlocked(Object):
    """
    Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked 

    Attributes:
        ID (:obj:`str`): ``ToggleMessageSenderIsBlocked``

    Args:
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of a message sender to block/unblock 
        is_blocked (:obj:`bool`):
            New value of is_blocked

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleMessageSenderIsBlocked"

    def __init__(self, sender_id, is_blocked, extra=None, **kwargs):
        self.extra = extra
        self.sender_id = sender_id  # MessageSender
        self.is_blocked = is_blocked  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleMessageSenderIsBlocked":
        sender_id = Object.read(q.get('sender_id'))
        is_blocked = q.get('is_blocked')
        return ToggleMessageSenderIsBlocked(sender_id, is_blocked)
