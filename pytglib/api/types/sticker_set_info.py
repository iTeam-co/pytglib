

from ..utils import Object


class StickerSetInfo(Object):
    """
    Represents short information about a sticker set

    Attributes:
        ID (:obj:`str`): ``StickerSetInfo``

    Args:
        id (:obj:`int`):
            Identifier of the sticker set 
        title (:obj:`str`):
            Title of the sticker set 
        name (:obj:`str`):
            Name of the sticker set 
        thumbnail (:class:`telegram.api.types.thumbnail`):
            Sticker set thumbnail in WEBP, TGS, or WEBM format with width and height 100; may be null
        thumbnail_outline (List of :class:`telegram.api.types.closedVectorPath`):
            Sticker set thumbnail's outline represented as a list of closed vector paths; may be emptyThe coordinate system origin is in the upper-left corner
        is_installed (:obj:`bool`):
            True, if the sticker set has been installed by the current user 
        is_archived (:obj:`bool`):
            True, if the sticker set has been archivedA sticker set can't be installed and archived simultaneously
        is_official (:obj:`bool`):
            True, if the sticker set is official 
        sticker_type (:class:`telegram.api.types.StickerType`):
            Type of the stickers in the set 
        is_viewed (:obj:`bool`):
            True for already viewed trending sticker sets
        size (:obj:`int`):
            Total number of stickers in the set 
        covers (List of :class:`telegram.api.types.sticker`):
            Up to the first 5 stickers from the set, depending on the contextIf the application needs more stickers the full sticker set needs to be requested

    Returns:
        StickerSetInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerSetInfo"

    def __init__(self, id, title, name, thumbnail, thumbnail_outline, is_installed, is_archived, is_official, sticker_type, is_viewed, size, covers, **kwargs):
        
        self.id = id  # int
        self.title = title  # str
        self.name = name  # str
        self.thumbnail = thumbnail  # Thumbnail
        self.thumbnail_outline = thumbnail_outline  # list of closedVectorPath
        self.is_installed = is_installed  # bool
        self.is_archived = is_archived  # bool
        self.is_official = is_official  # bool
        self.sticker_type = sticker_type  # StickerType
        self.is_viewed = is_viewed  # bool
        self.size = size  # int
        self.covers = covers  # list of sticker

    @staticmethod
    def read(q: dict, *args) -> "StickerSetInfo":
        id = q.get('id')
        title = q.get('title')
        name = q.get('name')
        thumbnail = Object.read(q.get('thumbnail'))
        thumbnail_outline = [Object.read(i) for i in q.get('thumbnail_outline', [])]
        is_installed = q.get('is_installed')
        is_archived = q.get('is_archived')
        is_official = q.get('is_official')
        sticker_type = Object.read(q.get('sticker_type'))
        is_viewed = q.get('is_viewed')
        size = q.get('size')
        covers = [Object.read(i) for i in q.get('covers', [])]
        return StickerSetInfo(id, title, name, thumbnail, thumbnail_outline, is_installed, is_archived, is_official, sticker_type, is_viewed, size, covers)
