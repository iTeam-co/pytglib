

from ..utils import Object


class GetStickerEmojis(Object):
    """
    Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object 

    Attributes:
        ID (:obj:`str`): ``GetStickerEmojis``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker file identifier

    Returns:
        Emojis

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStickerEmojis"

    def __init__(self, sticker, extra=None, **kwargs):
        self.extra = extra
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "GetStickerEmojis":
        sticker = Object.read(q.get('sticker'))
        return GetStickerEmojis(sticker)
