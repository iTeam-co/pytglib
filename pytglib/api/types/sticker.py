

from ..utils import Object


class Sticker(Object):
    """
    Describes a sticker 

    Attributes:
        ID (:obj:`str`): ``Sticker``

    Args:
        set_id (:obj:`int`):
            The identifier of the sticker set to which the sticker belongs; 0 if none 
        width (:obj:`int`):
            Sticker width; as defined by the sender 
        height (:obj:`int`):
            Sticker height; as defined by the sender
        emoji (:obj:`str`):
            Emoji corresponding to the sticker 
        is_animated (:obj:`bool`):
            True, if the sticker is an animated sticker in TGS format 
        is_mask (:obj:`bool`):
            True, if the sticker is a mask 
        mask_position (:class:`telegram.api.types.maskPosition`):
            Position where the mask should be placed; may be null 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Sticker thumbnail in WEBP or JPEG format; may be null 
        sticker (:class:`telegram.api.types.file`):
            File containing the sticker

    Returns:
        Sticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "sticker"

    def __init__(self, set_id, width, height, emoji, is_animated, is_mask, mask_position, thumbnail, sticker, **kwargs):
        
        self.set_id = set_id  # int
        self.width = width  # int
        self.height = height  # int
        self.emoji = emoji  # str
        self.is_animated = is_animated  # bool
        self.is_mask = is_mask  # bool
        self.mask_position = mask_position  # MaskPosition
        self.thumbnail = thumbnail  # PhotoSize
        self.sticker = sticker  # File

    @staticmethod
    def read(q: dict, *args) -> "Sticker":
        set_id = q.get('set_id')
        width = q.get('width')
        height = q.get('height')
        emoji = q.get('emoji')
        is_animated = q.get('is_animated')
        is_mask = q.get('is_mask')
        mask_position = Object.read(q.get('mask_position'))
        thumbnail = Object.read(q.get('thumbnail'))
        sticker = Object.read(q.get('sticker'))
        return Sticker(set_id, width, height, emoji, is_animated, is_mask, mask_position, thumbnail, sticker)
