

from ..utils import Object


class OpenChat(Object):
    """
    Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats) 

    Attributes:
        ID (:obj:`str`): ``OpenChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "openChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "OpenChat":
        chat_id = q.get('chat_id')
        return OpenChat(chat_id)
