

from ..utils import Object


class ChatFilterInfo(Object):
    """
    Contains basic information about a chat filter

    Attributes:
        ID (:obj:`str`): ``ChatFilterInfo``

    Args:
        id (:obj:`int`):
            Unique chat filter identifier
        title (:obj:`str`):
            The title of the filter; 1-12 characters without line feeds
        icon_name (:obj:`str`):
            The chosen or default icon name for short filter representationOne of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work", "Airplane", "Book", "Light", "Like", "Money", "Note", "Palette"

    Returns:
        ChatFilterInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatFilterInfo"

    def __init__(self, id, title, icon_name, **kwargs):
        
        self.id = id  # int
        self.title = title  # str
        self.icon_name = icon_name  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatFilterInfo":
        id = q.get('id')
        title = q.get('title')
        icon_name = q.get('icon_name')
        return ChatFilterInfo(id, title, icon_name)
