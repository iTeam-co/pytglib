

from ..utils import Object


class PushMessageContentContact(Object):
    """
    A message with a user contact 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentContact``

    Args:
        name (:obj:`str`):
            Contact's name 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentContact"

    def __init__(self, name, is_pinned, **kwargs):
        
        self.name = name  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentContact":
        name = q.get('name')
        is_pinned = q.get('is_pinned')
        return PushMessageContentContact(name, is_pinned)
