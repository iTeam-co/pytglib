

from ..utils import Object


class MessageForwardInfo(Object):
    """
    Contains information about a forwarded message

    Attributes:
        ID (:obj:`str`): ``MessageForwardInfo``

    Args:
        origin (:class:`telegram.api.types.MessageForwardOrigin`):
            Origin of a forwarded message
        date (:obj:`int`):
            Point in time (Unix timestamp) when the message was originally sent
        from_chat_id (:obj:`int`):
            For messages forwarded to the chat with the current user (Saved Messages) or to the channel's discussion group, the identifier of the chat from which the message was forwarded last time; 0 if unknown
        from_message_id (:obj:`int`):
            For messages forwarded to the chat with the current user (Saved Messages) or to the channel's discussion group, the identifier of the original message from which the new message was forwarded last time; 0 if unknown

    Returns:
        MessageForwardInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardInfo"

    def __init__(self, origin, date, from_chat_id, from_message_id, **kwargs):
        
        self.origin = origin  # MessageForwardOrigin
        self.date = date  # int
        self.from_chat_id = from_chat_id  # int
        self.from_message_id = from_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardInfo":
        origin = Object.read(q.get('origin'))
        date = q.get('date')
        from_chat_id = q.get('from_chat_id')
        from_message_id = q.get('from_message_id')
        return MessageForwardInfo(origin, date, from_chat_id, from_message_id)
