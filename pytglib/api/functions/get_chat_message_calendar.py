

from ..utils import Object


class GetChatMessageCalendar(Object):
    """
    Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"

    Attributes:
        ID (:obj:`str`): ``GetChatMessageCalendar``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to return information about messages
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Filter for message contentFilters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        from_message_id (:obj:`int`):
            The message identifier from which to return information about messages; use 0 to get results from the last message

    Returns:
        MessageCalendar

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatMessageCalendar"

    def __init__(self, chat_id, filter, from_message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.filter = filter  # SearchMessagesFilter
        self.from_message_id = from_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatMessageCalendar":
        chat_id = q.get('chat_id')
        filter = Object.read(q.get('filter'))
        from_message_id = q.get('from_message_id')
        return GetChatMessageCalendar(chat_id, filter, from_message_id)
