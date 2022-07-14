

from ..utils import Object


class GetAnimatedEmoji(Object):
    """
    Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji 

    Attributes:
        ID (:obj:`str`): ``GetAnimatedEmoji``

    Args:
        emoji (:obj:`str`):
            The emoji

    Returns:
        AnimatedEmoji

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAnimatedEmoji"

    def __init__(self, emoji, extra=None, **kwargs):
        self.extra = extra
        self.emoji = emoji  # str

    @staticmethod
    def read(q: dict, *args) -> "GetAnimatedEmoji":
        emoji = q.get('emoji')
        return GetAnimatedEmoji(emoji)
