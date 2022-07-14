

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
            Sticker thumbnail; pass null to skip thumbnail uploading 
        width (:obj:`int`):
            Sticker width 
        height (:obj:`int`):
            Sticker height 
        emoji (:obj:`str`):
            Emoji used to choose the sticker

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageSticker"

    def __init__(self, sticker, thumbnail, width, height, emoji, **kwargs):
        
        self.sticker = sticker  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.width = width  # int
        self.height = height  # int
        self.emoji = emoji  # str

    @staticmethod
    def read(q: dict, *args) -> "InputMessageSticker":
        sticker = Object.read(q.get('sticker'))
        thumbnail = Object.read(q.get('thumbnail'))
        width = q.get('width')
        height = q.get('height')
        emoji = q.get('emoji')
        return InputMessageSticker(sticker, thumbnail, width, height, emoji)
