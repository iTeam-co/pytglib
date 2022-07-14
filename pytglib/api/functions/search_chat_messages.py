

from ..utils import Object


class SearchChatMessages(Object):
    """
    Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query(searchSecretMessages must be used instead), or without an enabled message database. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    Attributes:
        ID (:obj:`str`): ``SearchChatMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to search messages
        query (:obj:`str`):
            Query to search for
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the sender of messages to search for; pass null to search for messages from any senderNot supported in secret chats
        from_message_id (:obj:`int`):
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        offset (:obj:`int`):
            Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
        limit (:obj:`int`):
            The maximum number of messages to be returned; must be positive and can't be greater than 100If the offset is negative, the limit must be greater than -offsetFor optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Additional filter for messages to search; pass null to search for all messages
        message_thread_id (:obj:`int`):
            If not 0, only messages in the specified thread will be returned; supergroups only

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatMessages"

    def __init__(self, chat_id, query, sender_id, from_message_id, offset, limit, filter, message_thread_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.sender_id = sender_id  # MessageSender
        self.from_message_id = from_message_id  # int
        self.offset = offset  # int
        self.limit = limit  # int
        self.filter = filter  # SearchMessagesFilter
        self.message_thread_id = message_thread_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchChatMessages":
        chat_id = q.get('chat_id')
        query = q.get('query')
        sender_id = Object.read(q.get('sender_id'))
        from_message_id = q.get('from_message_id')
        offset = q.get('offset')
        limit = q.get('limit')
        filter = Object.read(q.get('filter'))
        message_thread_id = q.get('message_thread_id')
        return SearchChatMessages(chat_id, query, sender_id, from_message_id, offset, limit, filter, message_thread_id)
