

from ..utils import Object


class MessageChatSetTheme(Object):
    """
    A theme in the chat has been changed 

    Attributes:
        ID (:obj:`str`): ``MessageChatSetTheme``

    Args:
        theme_name (:obj:`str`):
            If non-empty, name of a new theme, set for the chatOtherwise chat theme was reset to the default one

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatSetTheme"

    def __init__(self, theme_name, **kwargs):
        
        self.theme_name = theme_name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageChatSetTheme":
        theme_name = q.get('theme_name')
        return MessageChatSetTheme(theme_name)
