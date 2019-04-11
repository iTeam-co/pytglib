

from ..utils import Object


class Stickers(Object):
    """
    Represents a list of stickers 

    Attributes:
        ID (:obj:`str`): ``Stickers``

    Args:
        stickers (List of :class:`telegram.api.types.sticker`):
            List of stickers

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickers"

    def __init__(self, stickers, **kwargs):
        
        self.stickers = stickers  # list of sticker

    @staticmethod
    def read(q: dict, *args) -> "Stickers":
        stickers = [Object.read(i) for i in q.get('stickers', [])]
        return Stickers(stickers)
