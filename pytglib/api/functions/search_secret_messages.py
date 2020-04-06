

from ..utils import Object


class SearchSecretMessages(Object):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance the number of returned messages is chosen by the library

    Attributes:
        ID (:obj:`str`): ``SearchSecretMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to searchSpecify 0 to search in all secret chats 
        query (:obj:`str`):
            Query to search forIf empty, searchChatMessages should be used instead
        from_search_id (:obj:`int`):
            The identifier from the result of a previous request, use 0 to get results from the last message
        limit (:obj:`int`):
            The maximum number of messages to be returned; up to 100Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            A filter for the content of messages in the search results

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchSecretMessages"

    def __init__(self, chat_id, query, from_search_id, limit, filter, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.from_search_id = from_search_id  # int
        self.limit = limit  # int
        self.filter = filter  # SearchMessagesFilter

    @staticmethod
    def read(q: dict, *args) -> "SearchSecretMessages":
        chat_id = q.get('chat_id')
        query = q.get('query')
        from_search_id = q.get('from_search_id')
        limit = q.get('limit')
        filter = Object.read(q.get('filter'))
        return SearchSecretMessages(chat_id, query, from_search_id, limit, filter)
