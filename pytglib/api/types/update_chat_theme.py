

from ..utils import Object


class UpdateChatTheme(Object):
    """
    The chat theme was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatTheme``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        theme_name (:obj:`str`):
            The new name of the chat theme; may be empty if theme was reset to default

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatTheme"

    def __init__(self, chat_id, theme_name, **kwargs):
        
        self.chat_id = chat_id  # int
        self.theme_name = theme_name  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatTheme":
        chat_id = q.get('chat_id')
        theme_name = q.get('theme_name')
        return UpdateChatTheme(chat_id, theme_name)
