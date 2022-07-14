

from ..utils import Object


class SearchSecretMessages(Object):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib

    Attributes:
        ID (:obj:`str`): ``SearchSecretMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to searchSpecify 0 to search in all secret chats
        query (:obj:`str`):
            Query to search forIf empty, searchChatMessages must be used instead
        offset (:obj:`str`):
            Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        limit (:obj:`int`):
            The maximum number of messages to be returned; up to 100For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Additional filter for messages to search; pass null to search for all messages

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchSecretMessages"

    def __init__(self, chat_id, query, offset, limit, filter, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.offset = offset  # str
        self.limit = limit  # int
        self.filter = filter  # SearchMessagesFilter

    @staticmethod
    def read(q: dict, *args) -> "SearchSecretMessages":
        chat_id = q.get('chat_id')
        query = q.get('query')
        offset = q.get('offset')
        limit = q.get('limit')
        filter = Object.read(q.get('filter'))
        return SearchSecretMessages(chat_id, query, offset, limit, filter)
