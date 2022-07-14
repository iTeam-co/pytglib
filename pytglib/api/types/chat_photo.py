

from ..utils import Object


class ChatPhoto(Object):
    """
    Describes a chat or user profile photo

    Attributes:
        ID (:obj:`str`): ``ChatPhoto``

    Args:
        id (:obj:`int`):
            Unique photo identifier
        added_date (:obj:`int`):
            Point in time (Unix timestamp) when the photo has been added
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Photo minithumbnail; may be null
        sizes (List of :class:`telegram.api.types.photoSize`):
            Available variants of the photo in JPEG format, in different size
        animation (:class:`telegram.api.types.animatedChatPhoto`):
            A big (640x640) animated variant of the photo in MPEG4 format; may be null
        small_animation (:class:`telegram.api.types.animatedChatPhoto`):
            A small (160x160) animated variant of the photo in MPEG4 format; may be null even the big animation is available

    Returns:
        ChatPhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPhoto"

    def __init__(self, id, added_date, minithumbnail, sizes, animation, small_animation, **kwargs):
        
        self.id = id  # int
        self.added_date = added_date  # int
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.sizes = sizes  # list of photoSize
        self.animation = animation  # AnimatedChatPhoto
        self.small_animation = small_animation  # AnimatedChatPhoto

    @staticmethod
    def read(q: dict, *args) -> "ChatPhoto":
        id = q.get('id')
        added_date = q.get('added_date')
        minithumbnail = Object.read(q.get('minithumbnail'))
        sizes = [Object.read(i) for i in q.get('sizes', [])]
        animation = Object.read(q.get('animation'))
        small_animation = Object.read(q.get('small_animation'))
        return ChatPhoto(id, added_date, minithumbnail, sizes, animation, small_animation)
