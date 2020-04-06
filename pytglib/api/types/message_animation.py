

from ..utils import Object


class MessageAnimation(Object):
    """
    An animation message (GIF-style). 

    Attributes:
        ID (:obj:`str`): ``MessageAnimation``

    Args:
        animation (:class:`telegram.api.types.animation`):
            The animation description 
        caption (:class:`telegram.api.types.formattedText`):
            Animation caption 
        is_secret (:obj:`bool`):
            True, if the animation thumbnail must be blurred and the animation must be shown only while tapped

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageAnimation"

    def __init__(self, animation, caption, is_secret, **kwargs):
        
        self.animation = animation  # Animation
        self.caption = caption  # FormattedText
        self.is_secret = is_secret  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageAnimation":
        animation = Object.read(q.get('animation'))
        caption = Object.read(q.get('caption'))
        is_secret = q.get('is_secret')
        return MessageAnimation(animation, caption, is_secret)
