

from ..utils import Object


class MessageFileTypeUnknown(Object):
    """
    The messages was exported from a chat of unknown type

    Attributes:
        ID (:obj:`str`): ``MessageFileTypeUnknown``

    No parameters required.

    Returns:
        MessageFileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageFileTypeUnknown"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageFileTypeUnknown":
        
        return MessageFileTypeUnknown()
