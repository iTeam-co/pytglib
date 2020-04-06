

from ..utils import Object


class SearchChatRecentLocationMessages(Object):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user 

    Attributes:
        ID (:obj:`str`): ``SearchChatRecentLocationMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        limit (:obj:`int`):
            The maximum number of messages to be returned

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatRecentLocationMessages"

    def __init__(self, chat_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "SearchChatRecentLocationMessages":
        chat_id = q.get('chat_id')
        limit = q.get('limit')
        return SearchChatRecentLocationMessages(chat_id, limit)
