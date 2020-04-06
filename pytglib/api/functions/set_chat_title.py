

from ..utils import Object


class SetChatTitle(Object):
    """
    Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info rights. The title will not be changed until the request to the server has been completed

    Attributes:
        ID (:obj:`str`): ``SetChatTitle``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        title (:obj:`str`):
            New title of the chat; 1-128 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatTitle"

    def __init__(self, chat_id, title, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "SetChatTitle":
        chat_id = q.get('chat_id')
        title = q.get('title')
        return SetChatTitle(chat_id, title)
