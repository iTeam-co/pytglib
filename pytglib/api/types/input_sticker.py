

from ..utils import Object


class InputSticker(Object):
    """
    A sticker to be added to a sticker set

    Attributes:
        ID (:obj:`str`): ``InputSticker``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            File with the sticker; must fit in a 512x512 squareFor WEBP stickers and masks the file must be in PNG format, which will be converted to WEBP server-sideOtherwise, the file must be local or uploaded within a weekSee https://coretelegramorg/animated_stickers#technical-requirements for technical requirements
        emojis (:obj:`str`):
            Emojis corresponding to the sticker
        type (:class:`telegram.api.types.StickerType`):
            Sticker type

    Returns:
        InputSticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputSticker"

    def __init__(self, sticker, emojis, type, **kwargs):
        
        self.sticker = sticker  # InputFile
        self.emojis = emojis  # str
        self.type = type  # StickerType

    @staticmethod
    def read(q: dict, *args) -> "InputSticker":
        sticker = Object.read(q.get('sticker'))
        emojis = q.get('emojis')
        type = Object.read(q.get('type'))
        return InputSticker(sticker, emojis, type)
