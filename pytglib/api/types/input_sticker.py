

from ..utils import Object


class InputSticker(Object):
    """
    Describes a sticker that should be added to a sticker set 

    Attributes:
        ID (:obj:`str`): ``InputSticker``

    Args:
        png_sticker (:class:`telegram.api.types.InputFile`):
            PNG image with the sticker; must be up to 512 kB in size and fit in a 512x512 square 
        emojis (:obj:`str`):
            Emoji corresponding to the sticker 
        mask_position (:class:`telegram.api.types.maskPosition`):
            For masks, position where the mask should be placed; may be null

    Returns:
        InputSticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputSticker"

    def __init__(self, png_sticker, emojis, mask_position, **kwargs):
        
        self.png_sticker = png_sticker  # InputFile
        self.emojis = emojis  # str
        self.mask_position = mask_position  # MaskPosition

    @staticmethod
    def read(q: dict, *args) -> "InputSticker":
        png_sticker = Object.read(q.get('png_sticker'))
        emojis = q.get('emojis')
        mask_position = Object.read(q.get('mask_position'))
        return InputSticker(png_sticker, emojis, mask_position)
