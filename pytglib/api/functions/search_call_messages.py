

from ..utils import Object


class SearchCallMessages(Object):
    """
    Searches for call messages. Returns the results in reverse chronological order (i. e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

    Attributes:
        ID (:obj:`str`): ``SearchCallMessages``

    Args:
        from_message_id (:obj:`int`):
            Identifier of the message from which to search; use 0 to get results from the last message
        limit (:obj:`int`):
            The maximum number of messages to be returned; up to 100For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        only_missed (:obj:`bool`):
            Pass true to search only for messages with missed/declined calls

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchCallMessages"

    def __init__(self, from_message_id, limit, only_missed, extra=None, **kwargs):
        self.extra = extra
        self.from_message_id = from_message_id  # int
        self.limit = limit  # int
        self.only_missed = only_missed  # bool

    @staticmethod
    def read(q: dict, *args) -> "SearchCallMessages":
        from_message_id = q.get('from_message_id')
        limit = q.get('limit')
        only_missed = q.get('only_missed')
        return SearchCallMessages(from_message_id, limit, only_missed)
