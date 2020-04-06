

from ..utils import Object


class ChatPhoto(Object):
    """
    Describes the photo of a chat 

    Attributes:
        ID (:obj:`str`): ``ChatPhoto``

    Args:
        small (:class:`telegram.api.types.file`):
            A small (160x160) chat photoThe file can be downloaded only before the photo is changed 
        big (:class:`telegram.api.types.file`):
            A big (640x640) chat photoThe file can be downloaded only before the photo is changed

    Returns:
        ChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPhoto"

    def __init__(self, small, big, **kwargs):
        
        self.small = small  # File
        self.big = big  # File

    @staticmethod
    def read(q: dict, *args) -> "ChatPhoto":
        small = Object.read(q.get('small'))
        big = Object.read(q.get('big'))
        return ChatPhoto(small, big)
