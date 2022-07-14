

from ..utils import Object


class MessageFileTypePrivate(Object):
    """
    The messages was exported from a private chat 

    Attributes:
        ID (:obj:`str`): ``MessageFileTypePrivate``

    Args:
        name (:obj:`str`):
            Name of the other party; may be empty if unrecognized

    Returns:
        MessageFileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageFileTypePrivate"

    def __init__(self, name, **kwargs):
        
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageFileTypePrivate":
        name = q.get('name')
        return MessageFileTypePrivate(name)
