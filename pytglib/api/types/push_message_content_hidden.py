

from ..utils import Object


class PushMessageContentHidden(Object):
    """
    A general message with hidden content 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentHidden``

    Args:
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentHidden"

    def __init__(self, is_pinned, **kwargs):
        
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentHidden":
        is_pinned = q.get('is_pinned')
        return PushMessageContentHidden(is_pinned)
