

from ..utils import Object


class PushMessageContentGame(Object):
    """
    A message with a game 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentGame``

    Args:
        title (:obj:`str`):
            Game title, empty for pinned game message 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentGame"

    def __init__(self, title, is_pinned, **kwargs):
        
        self.title = title  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentGame":
        title = q.get('title')
        is_pinned = q.get('is_pinned')
        return PushMessageContentGame(title, is_pinned)
