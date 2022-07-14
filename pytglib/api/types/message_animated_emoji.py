

from ..utils import Object


class MessageAnimatedEmoji(Object):
    """
    A message with an animated emoji 

    Attributes:
        ID (:obj:`str`): ``MessageAnimatedEmoji``

    Args:
        animated_emoji (:class:`telegram.api.types.animatedEmoji`):
            The animated emoji 
        emoji (:obj:`str`):
            The corresponding emoji

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageAnimatedEmoji"

    def __init__(self, animated_emoji, emoji, **kwargs):
        
        self.animated_emoji = animated_emoji  # AnimatedEmoji
        self.emoji = emoji  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageAnimatedEmoji":
        animated_emoji = Object.read(q.get('animated_emoji'))
        emoji = q.get('emoji')
        return MessageAnimatedEmoji(animated_emoji, emoji)
