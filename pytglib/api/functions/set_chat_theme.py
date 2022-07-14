

from ..utils import Object


class SetChatTheme(Object):
    """
    Changes the chat theme. Supported only in private and secret chats 

    Attributes:
        ID (:obj:`str`): ``SetChatTheme``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        theme_name (:obj:`str`):
            Name of the new chat theme; pass an empty string to return the default theme

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatTheme"

    def __init__(self, chat_id, theme_name, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.theme_name = theme_name  # str

    @staticmethod
    def read(q: dict, *args) -> "SetChatTheme":
        chat_id = q.get('chat_id')
        theme_name = q.get('theme_name')
        return SetChatTheme(chat_id, theme_name)
