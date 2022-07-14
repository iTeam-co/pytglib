

from ..utils import Object


class SearchOutgoingDocumentMessages(Object):
    """
    Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order

    Attributes:
        ID (:obj:`str`): ``SearchOutgoingDocumentMessages``

    Args:
        query (:obj:`str`):
            Query to search for in document file name and message caption
        limit (:obj:`int`):
            The maximum number of messages to be returned; up to 100

    Returns:
        FoundMessages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchOutgoingDocumentMessages"

    def __init__(self, query, limit, extra=None, **kwargs):
        self.extra = extra
        self.query = query  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchOutgoingDocumentMessages":
        query = q.get('query')
        limit = q.get('limit')
        return SearchOutgoingDocumentMessages(query, limit)
