

from ..utils import Object


class GetChatMessageCount(Object):
    """
    Returns approximate number of messages of the specified type in the chat 

    Attributes:
        ID (:obj:`str`): ``GetChatMessageCount``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat in which to count messages 
        filter (:class:`telegram.api.types.SearchMessagesFilter`):
            Filter for message content; searchMessagesFilterEmpty is unsupported in this function 
        return_local (:obj:`bool`):
            If true, returns count that is available locally without sending network requests, returning -1 if the number of messages is unknown

    Returns:
        Count

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatMessageCount"

    def __init__(self, chat_id, filter, return_local, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.filter = filter  # SearchMessagesFilter
        self.return_local = return_local  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetChatMessageCount":
        chat_id = q.get('chat_id')
        filter = Object.read(q.get('filter'))
        return_local = q.get('return_local')
        return GetChatMessageCount(chat_id, filter, return_local)
