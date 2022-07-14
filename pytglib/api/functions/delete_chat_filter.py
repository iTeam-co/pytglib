

from ..utils import Object


class DeleteChatFilter(Object):
    """
    Deletes existing chat filter 

    Attributes:
        ID (:obj:`str`): ``DeleteChatFilter``

    Args:
        chat_filter_id (:obj:`int`):
            Chat filter identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatFilter"

    def __init__(self, chat_filter_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_filter_id = chat_filter_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatFilter":
        chat_filter_id = q.get('chat_filter_id')
        return DeleteChatFilter(chat_filter_id)
