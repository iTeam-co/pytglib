

from ..utils import Object


class GetAllAnimatedEmojis(Object):
    """
    Returns all emojis, which has a corresponding animated emoji

    Attributes:
        ID (:obj:`str`): ``GetAllAnimatedEmojis``

    No parameters required.

    Returns:
        Emojis

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAllAnimatedEmojis"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetAllAnimatedEmojis":
        
        return GetAllAnimatedEmojis()
