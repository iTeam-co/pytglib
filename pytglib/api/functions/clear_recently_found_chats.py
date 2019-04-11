

from ..utils import Object


class ClearRecentlyFoundChats(Object):
    """
    Clears the list of recently found chats

    Attributes:
        ID (:obj:`str`): ``ClearRecentlyFoundChats``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "clearRecentlyFoundChats"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ClearRecentlyFoundChats":
        
        return ClearRecentlyFoundChats()
