

from ..utils import Object


class UpdateChatTitle(Object):
    """
    The title of a chat was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatTitle``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        title (:obj:`str`):
            The new chat title

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatTitle"

    def __init__(self, chat_id, title, **kwargs):
        
        self.chat_id = chat_id  # int
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatTitle":
        chat_id = q.get('chat_id')
        title = q.get('title')
        return UpdateChatTitle(chat_id, title)
