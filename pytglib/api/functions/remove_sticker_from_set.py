

from ..utils import Object


class RemoveStickerFromSet(Object):
    """
    Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot 

    Attributes:
        ID (:obj:`str`): ``RemoveStickerFromSet``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeStickerFromSet"

    def __init__(self, sticker, extra=None, **kwargs):
        self.extra = extra
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "RemoveStickerFromSet":
        sticker = Object.read(q.get('sticker'))
        return RemoveStickerFromSet(sticker)
