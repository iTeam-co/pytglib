

from ..utils import Object


class StickerEmojis(Object):
    """
    Represents a list of all emoji corresponding to a sticker in a sticker set. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object 

    Attributes:
        ID (:obj:`str`): ``StickerEmojis``

    Args:
        emojis (List of :obj:`str`):
            List of emojis

    Returns:
        StickerEmojis

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerEmojis"

    def __init__(self, emojis, **kwargs):
        
        self.emojis = emojis  # list of str

    @staticmethod
    def read(q: dict, *args) -> "StickerEmojis":
        emojis = q.get('emojis')
        return StickerEmojis(emojis)
