

from ..utils import Object


class InputMessageSticker(Object):
    """
    A sticker message 

    Attributes:
        ID (:obj:`str`): ``InputMessageSticker``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker to be sent 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Sticker thumbnail, if available 
        width (:obj:`int`):
            Sticker width 
        height (:obj:`int`):
            Sticker height

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageSticker"

    def __init__(self, sticker, thumbnail, width, height, **kwargs):
        
        self.sticker = sticker  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.width = width  # int
        self.height = height  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessageSticker":
        sticker = Object.read(q.get('sticker'))
        thumbnail = Object.read(q.get('thumbnail'))
        width = q.get('width')
        height = q.get('height')
        return InputMessageSticker(sticker, thumbnail, width, height)
