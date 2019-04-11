

from ..utils import Object


class GetChatAdministrators(Object):
    """
    Returns a list of users who are administrators of the chat 

    Attributes:
        ID (:obj:`str`): ``GetChatAdministrators``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatAdministrators"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatAdministrators":
        chat_id = q.get('chat_id')
        return GetChatAdministrators(chat_id)
