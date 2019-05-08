

from ..utils import Object


class CloseChat(Object):
    """
    Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed 

    Attributes:
        ID (:obj:`str`): ``CloseChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "closeChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CloseChat":
        chat_id = q.get('chat_id')
        return CloseChat(chat_id)
