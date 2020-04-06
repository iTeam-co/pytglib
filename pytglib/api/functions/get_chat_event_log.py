

from ..utils import Object


class GetChatEventLog(Object):
    """
    Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i. e., in order of decreasing event_id)

    Attributes:
        ID (:obj:`str`): ``GetChatEventLog``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        query (:obj:`str`):
            Search query by which to filter events 
        from_event_id (:obj:`int`):
            Identifier of an event from which to return resultsUse 0 to get results from the latest events 
        limit (:obj:`int`):
            The maximum number of events to return; up to 100
        filters (:class:`telegram.api.types.chatEventLogFilters`):
            The types of events to returnBy default, all types will be returned 
        user_ids (List of :obj:`int`):
            User identifiers by which to filter eventsBy default, events relating to all users will be returned

    Returns:
        ChatEvents

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatEventLog"

    def __init__(self, chat_id, query, from_event_id, limit, filters, user_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.query = query  # str
        self.from_event_id = from_event_id  # int
        self.limit = limit  # int
        self.filters = filters  # ChatEventLogFilters
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "GetChatEventLog":
        chat_id = q.get('chat_id')
        query = q.get('query')
        from_event_id = q.get('from_event_id')
        limit = q.get('limit')
        filters = Object.read(q.get('filters'))
        user_ids = q.get('user_ids')
        return GetChatEventLog(chat_id, query, from_event_id, limit, filters, user_ids)
