

from ..utils import Object


class PushMessageContentGameScore(Object):
    """
    A new high score was achieved in a game 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentGameScore``

    Args:
        title (:obj:`str`):
            Game title, empty for pinned message 
        score (:obj:`int`):
            New score, 0 for pinned message 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentGameScore"

    def __init__(self, title, score, is_pinned, **kwargs):
        
        self.title = title  # str
        self.score = score  # int
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentGameScore":
        title = q.get('title')
        score = q.get('score')
        is_pinned = q.get('is_pinned')
        return PushMessageContentGameScore(title, score, is_pinned)
