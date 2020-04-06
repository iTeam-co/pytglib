

from ..utils import Object


class InputStickerAnimated(Object):
    """
    An animated sticker in TGS format

    Attributes:
        ID (:obj:`str`): ``InputStickerAnimated``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            File with the animated stickerOnly local or uploaded within a week files are supportedSee https://coretelegramorg/animated_stickers#technical-requirements for technical requirements
        emojis (:obj:`str`):
            Emojis corresponding to the sticker

    Returns:
        InputSticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputStickerAnimated"

    def __init__(self, sticker, emojis, **kwargs):
        
        self.sticker = sticker  # InputFile
        self.emojis = emojis  # str

    @staticmethod
    def read(q: dict, *args) -> "InputStickerAnimated":
        sticker = Object.read(q.get('sticker'))
        emojis = q.get('emojis')
        return InputStickerAnimated(sticker, emojis)
