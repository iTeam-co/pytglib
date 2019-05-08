

from ..utils import Object


class PushMessageContentLocation(Object):
    """
    A message with a location 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentLocation``

    Args:
        is_live (:obj:`bool`):
            True, if the location is live 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentLocation"

    def __init__(self, is_live, is_pinned, **kwargs):
        
        self.is_live = is_live  # bool
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentLocation":
        is_live = q.get('is_live')
        is_pinned = q.get('is_pinned')
        return PushMessageContentLocation(is_live, is_pinned)
