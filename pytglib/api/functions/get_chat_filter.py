

from ..utils import Object


class GetChatFilter(Object):
    """
    Returns information about a chat filter by its identifier 

    Attributes:
        ID (:obj:`str`): ``GetChatFilter``

    Args:
        chat_filter_id (:obj:`int`):
            Chat filter identifier

    Returns:
        ChatFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatFilter"

    def __init__(self, chat_filter_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_filter_id = chat_filter_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatFilter":
        chat_filter_id = q.get('chat_filter_id')
        return GetChatFilter(chat_filter_id)
