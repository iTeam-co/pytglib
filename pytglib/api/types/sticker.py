

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
        type (:class:`telegram.api.types.StickerType`):
            Sticker type 
        outline (List of :class:`telegram.api.types.closedVectorPath`):
            Sticker's outline represented as a list of closed vector paths; may be emptyThe coordinate system origin is in the upper-left corner
        thumbnail (:class:`telegram.api.types.thumbnail`):
            Sticker thumbnail in WEBP or JPEG format; may be null 
        premium_animation (:class:`telegram.api.types.file`):
            Premium animation of the sticker; may be nullIf present, only Premium users can send the sticker 
        sticker (:class:`telegram.api.types.file`):
            File containing the sticker

    Returns:
        Sticker

    Raises:
        :class:`telegram.Error`
    """
    ID = "sticker"

    def __init__(self, set_id, width, height, emoji, type, outline, thumbnail, premium_animation, sticker, **kwargs):
        
        self.set_id = set_id  # int
        self.width = width  # int
        self.height = height  # int
        self.emoji = emoji  # str
        self.type = type  # StickerType
        self.outline = outline  # list of closedVectorPath
        self.thumbnail = thumbnail  # Thumbnail
        self.premium_animation = premium_animation  # File
        self.sticker = sticker  # File

    @staticmethod
    def read(q: dict, *args) -> "Sticker":
        set_id = q.get('set_id')
        width = q.get('width')
        height = q.get('height')
        emoji = q.get('emoji')
        type = Object.read(q.get('type'))
        outline = [Object.read(i) for i in q.get('outline', [])]
        thumbnail = Object.read(q.get('thumbnail'))
        premium_animation = Object.read(q.get('premium_animation'))
        sticker = Object.read(q.get('sticker'))
        return Sticker(set_id, width, height, emoji, type, outline, thumbnail, premium_animation, sticker)
