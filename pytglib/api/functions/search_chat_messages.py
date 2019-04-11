

from ..utils import Object


class SearchChatMessages(Object):
    """
    Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query(searchSecretMessages should be used instead), or without an enabled message database. For optimal performance the number of returned messages is chosen by the library

    Attributes:
        ID (:obj:`str`): ``SearchChatMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to search messages
        query (:obj:`str`):
            Query to search for
        sender_user_id (:obj:`int`):
            If not 0, only messages sent by the specified user will be returnedNot supported in secret chats
        from_message_id (:obj:`int`):
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        offset (:obj:`int`):
            Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
        limit (:obj:`int`):
            The maximum number of messages to be returned; must be positive and can't be greater than 100If the offset is negative, the limit must be greater than -offsetFewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Filter for message content in the search results

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatMessages"

    def __init__(self, chat_id, query, sender_user_id, from_message_id, offset, limit, filter, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.sender_user_id = sender_user_id  # int
        self.from_message_id = from_message_id  # int
        self.offset = offset  # int
        self.limit = limit  # int
        self.filter = filter  # SearchMessagesFilter

    @staticmethod
    def read(q: dict, *args) -> "SearchChatMessages":
        chat_id = q.get('chat_id')
        query = q.get('query')
        sender_user_id = q.get('sender_user_id')
        from_message_id = q.get('from_message_id')
        offset = q.get('offset')
        limit = q.get('limit')
        filter = Object.read(q.get('filter'))
        return SearchChatMessages(chat_id, query, sender_user_id, from_message_id, offset, limit, filter)
