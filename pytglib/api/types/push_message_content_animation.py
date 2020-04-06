

from ..utils import Object


class PushMessageContentAnimation(Object):
    """
    An animation message (GIF-style). 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentAnimation``

    Args:
        animation (:class:`telegram.api.types.animation`):
            Message content; may be null 
        caption (:obj:`str`):
            Animation caption 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentAnimation"

    def __init__(self, animation, caption, is_pinned, **kwargs):
        
        self.animation = animation  # Animation
        self.caption = caption  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentAnimation":
        animation = Object.read(q.get('animation'))
        caption = q.get('caption')
        is_pinned = q.get('is_pinned')
        return PushMessageContentAnimation(animation, caption, is_pinned)
