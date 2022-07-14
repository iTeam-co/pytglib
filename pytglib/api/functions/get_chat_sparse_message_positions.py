

from ..utils import Object


class GetChatSparseMessagePositions(Object):
    """
    Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id).Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

    Attributes:
        ID (:obj:`str`): ``GetChatSparseMessagePositions``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to return information about message positions
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Filter for message contentFilters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        from_message_id (:obj:`int`):
            The message identifier from which to return information about message positions
        limit (:obj:`int`):
            The expected number of message positions to be returned; 50-2000A smaller number of positions can be returned, if there are not enough appropriate messages

    Returns:
        MessagePositions

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatSparseMessagePositions"

    def __init__(self, chat_id, filter, from_message_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.filter = filter  # SearchMessagesFilter
        self.from_message_id = from_message_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatSparseMessagePositions":
        chat_id = q.get('chat_id')
        filter = Object.read(q.get('filter'))
        from_message_id = q.get('from_message_id')
        limit = q.get('limit')
        return GetChatSparseMessagePositions(chat_id, filter, from_message_id, limit)
