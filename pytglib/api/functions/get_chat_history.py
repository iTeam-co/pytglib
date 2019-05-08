

from ..utils import Object


class GetChatHistory(Object):
    """
    Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id).For optimal performance the number of returned messages is chosen by the library. This is an offline request if only_local is true

    Attributes:
        ID (:obj:`str`): ``GetChatHistory``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        from_message_id (:obj:`int`):
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        offset (:obj:`int`):
            Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        limit (:obj:`int`):
            The maximum number of messages to be returned; must be positive and can't be greater than 100If the offset is negative, the limit must be greater or equal to -offsetFewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        only_local (:obj:`bool`):
            If true, returns only messages that are available locally without sending network requests

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatHistory"

    def __init__(self, chat_id, from_message_id, offset, limit, only_local, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.from_message_id = from_message_id  # int
        self.offset = offset  # int
        self.limit = limit  # int
        self.only_local = only_local  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetChatHistory":
        chat_id = q.get('chat_id')
        from_message_id = q.get('from_message_id')
        offset = q.get('offset')
        limit = q.get('limit')
        only_local = q.get('only_local')
        return GetChatHistory(chat_id, from_message_id, offset, limit, only_local)
