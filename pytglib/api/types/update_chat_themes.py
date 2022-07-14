

from ..utils import Object


class UpdateChatThemes(Object):
    """
    The list of available chat themes has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatThemes``

    Args:
        chat_themes (List of :class:`telegram.api.types.chatTheme`):
            The new list of chat themes

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatThemes"

    def __init__(self, chat_themes, **kwargs):
        
        self.chat_themes = chat_themes  # list of chatTheme

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatThemes":
        chat_themes = [Object.read(i) for i in q.get('chat_themes', [])]
        return UpdateChatThemes(chat_themes)
