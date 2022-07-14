

from ..utils import Object


class GetMessageThreadHistory(Object):
    """
    Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup.The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

    Attributes:
        ID (:obj:`str`): ``GetMessageThreadHistory``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        message_id (:obj:`int`):
            Message identifier, which thread history needs to be returned
        from_message_id (:obj:`int`):
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        offset (:obj:`int`):
            Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        limit (:obj:`int`):
            The maximum number of messages to be returned; must be positive and can't be greater than 100If the offset is negative, the limit must be greater than or equal to -offsetFor optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageThreadHistory"

    def __init__(self, chat_id, message_id, from_message_id, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.from_message_id = from_message_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageThreadHistory":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        from_message_id = q.get('from_message_id')
        offset = q.get('offset')
        limit = q.get('limit')
        return GetMessageThreadHistory(chat_id, message_id, from_message_id, offset, limit)
