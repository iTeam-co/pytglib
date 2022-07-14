

from ..utils import Object


class ChatPhotoInfo(Object):
    """
    Contains basic information about the photo of a chat

    Attributes:
        ID (:obj:`str`): ``ChatPhotoInfo``

    Args:
        small (:class:`telegram.api.types.file`):
            A small (160x160) chat photo variant in JPEG formatThe file can be downloaded only before the photo is changed
        big (:class:`telegram.api.types.file`):
            A big (640x640) chat photo variant in JPEG formatThe file can be downloaded only before the photo is changed
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Chat photo minithumbnail; may be null
        has_animation (:obj:`bool`):
            True, if the photo has animated variant

    Returns:
        ChatPhotoInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPhotoInfo"

    def __init__(self, small, big, minithumbnail, has_animation, **kwargs):
        
        self.small = small  # File
        self.big = big  # File
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.has_animation = has_animation  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatPhotoInfo":
        small = Object.read(q.get('small'))
        big = Object.read(q.get('big'))
        minithumbnail = Object.read(q.get('minithumbnail'))
        has_animation = q.get('has_animation')
        return ChatPhotoInfo(small, big, minithumbnail, has_animation)
