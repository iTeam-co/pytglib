

from ..utils import Object


class PushMessageContentText(Object):
    """
    A text message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentText``

    Args:
        text (:obj:`str`):
            Message text 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentText"

    def __init__(self, text, is_pinned, **kwargs):
        
        self.text = text  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentText":
        text = q.get('text')
        is_pinned = q.get('is_pinned')
        return PushMessageContentText(text, is_pinned)
