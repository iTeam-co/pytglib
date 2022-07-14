

from ..utils import Object


class PushMessageContentChatSetTheme(Object):
    """
    A chat theme was edited 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatSetTheme``

    Args:
        theme_name (:obj:`str`):
            If non-empty, name of a new theme, set for the chatOtherwise chat theme was reset to the default one

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatSetTheme"

    def __init__(self, theme_name, **kwargs):
        
        self.theme_name = theme_name  # str

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatSetTheme":
        theme_name = q.get('theme_name')
        return PushMessageContentChatSetTheme(theme_name)
