

from ..utils import Object


class GetMessagePublicForwards(Object):
    """
    Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib

    Attributes:
        ID (:obj:`str`): ``GetMessagePublicForwards``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message
        message_id (:obj:`int`):
            Message identifier
        offset (:obj:`str`):
            Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        limit (:obj:`int`):
            The maximum number of messages to be returned; must be positive and can't be greater than 100For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessagePublicForwards"

    def __init__(self, chat_id, message_id, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.offset = offset  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessagePublicForwards":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        offset = q.get('offset')
        limit = q.get('limit')
        return GetMessagePublicForwards(chat_id, message_id, offset, limit)
