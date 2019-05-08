

from ..utils import Object


class PushMessageContentDocument(Object):
    """
    A document message (a general file) 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentDocument``

    Args:
        document (:class:`telegram.api.types.document`):
            Message content; may be null 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentDocument"

    def __init__(self, document, is_pinned, **kwargs):
        
        self.document = document  # Document
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentDocument":
        document = Object.read(q.get('document'))
        is_pinned = q.get('is_pinned')
        return PushMessageContentDocument(document, is_pinned)
