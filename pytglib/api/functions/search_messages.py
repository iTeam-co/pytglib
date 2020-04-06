

from ..utils import Object


class SearchMessages(Object):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)).For optimal performance the number of returned messages is chosen by the library

    Attributes:
        ID (:obj:`str`): ``SearchMessages``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            Chat list in which to search messages; pass null to search in all chats regardless of their chat list
        query (:obj:`str`):
            Query to search for
        offset_date (:obj:`int`):
            The date of the message starting from which the results should be fetchedUse 0 or any date in the future to get results from the last message
        offset_chat_id (:obj:`int`):
            The chat identifier of the last found message, or 0 for the first request
        offset_message_id (:obj:`int`):
            The message identifier of the last found message, or 0 for the first request
        limit (:obj:`int`):
            The maximum number of messages to be returned, up to 100Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchMessages"

    def __init__(self, chat_list, query, offset_date, offset_chat_id, offset_message_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_list = chat_list  # ChatList
        self.query = query  # str
        self.offset_date = offset_date  # int
        self.offset_chat_id = offset_chat_id  # int
        self.offset_message_id = offset_message_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchMessages":
        chat_list = Object.read(q.get('chat_list'))
        query = q.get('query')
        offset_date = q.get('offset_date')
        offset_chat_id = q.get('offset_chat_id')
        offset_message_id = q.get('offset_message_id')
        limit = q.get('limit')
        return SearchMessages(chat_list, query, offset_date, offset_chat_id, offset_message_id, limit)
