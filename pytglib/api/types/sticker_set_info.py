

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
        thumbnail (:class:`telegram.api.types.photoSize`):
            Sticker set thumbnail in WEBP format with width and height 100; may be null
        is_installed (:obj:`bool`):
            True, if the sticker set has been installed by current user 
        is_archived (:obj:`bool`):
            True, if the sticker set has been archivedA sticker set can't be installed and archived simultaneously
        is_official (:obj:`bool`):
            True, if the sticker set is official 
        is_animated (:obj:`bool`):
            True, is the stickers in the set are animated 
        is_masks (:obj:`bool`):
            True, if the stickers in the set are masks 
        is_viewed (:obj:`bool`):
            True for already viewed trending sticker sets
        size (:obj:`int`):
            Total number of stickers in the set 
        covers (List of :class:`telegram.api.types.sticker`):
            Contains up to the first 5 stickers from the set, depending on the contextIf the client needs more stickers the full set should be requested

    Returns:
        StickerSetInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerSetInfo"

    def __init__(self, id, title, name, thumbnail, is_installed, is_archived, is_official, is_animated, is_masks, is_viewed, size, covers, **kwargs):
        
        self.id = id  # int
        self.title = title  # str
        self.name = name  # str
        self.thumbnail = thumbnail  # PhotoSize
        self.is_installed = is_installed  # bool
        self.is_archived = is_archived  # bool
        self.is_official = is_official  # bool
        self.is_animated = is_animated  # bool
        self.is_masks = is_masks  # bool
        self.is_viewed = is_viewed  # bool
        self.size = size  # int
        self.covers = covers  # list of sticker

    @staticmethod
    def read(q: dict, *args) -> "StickerSetInfo":
        id = q.get('id')
        title = q.get('title')
        name = q.get('name')
        thumbnail = Object.read(q.get('thumbnail'))
        is_installed = q.get('is_installed')
        is_archived = q.get('is_archived')
        is_official = q.get('is_official')
        is_animated = q.get('is_animated')
        is_masks = q.get('is_masks')
        is_viewed = q.get('is_viewed')
        size = q.get('size')
        covers = [Object.read(i) for i in q.get('covers', [])]
        return StickerSetInfo(id, title, name, thumbnail, is_installed, is_archived, is_official, is_animated, is_masks, is_viewed, size, covers)
