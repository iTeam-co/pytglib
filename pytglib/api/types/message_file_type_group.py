

from ..utils import Object


class MessageFileTypeGroup(Object):
    """
    The messages was exported from a group chat 

    Attributes:
        ID (:obj:`str`): ``MessageFileTypeGroup``

    Args:
        title (:obj:`str`):
            Title of the group chat; may be empty if unrecognized

    Returns:
        MessageFileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageFileTypeGroup"

    def __init__(self, title, **kwargs):
        
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageFileTypeGroup":
        title = q.get('title')
        return MessageFileTypeGroup(title)
