

from ..utils import Object


class InputStickerStatic(Object):
    """
    A static sticker in PNG format, which will be converted to WEBP server-side

    Attributes:
        ID (:obj:`str`): ``InputStickerStatic``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            PNG image with the sticker; must be up to 512 KB in size and fit in a 512x512 square
        emojis (:obj:`str`):
            Emojis corresponding to the sticker
        mask_position (:class:`telegram.api.types.maskPosition`):
            For masks, position where the mask should be placed; may be null

    Returns:
        InputSticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputStickerStatic"

    def __init__(self, sticker, emojis, mask_position, **kwargs):
        
        self.sticker = sticker  # InputFile
        self.emojis = emojis  # str
        self.mask_position = mask_position  # MaskPosition

    @staticmethod
    def read(q: dict, *args) -> "InputStickerStatic":
        sticker = Object.read(q.get('sticker'))
        emojis = q.get('emojis')
        mask_position = Object.read(q.get('mask_position'))
        return InputStickerStatic(sticker, emojis, mask_position)
