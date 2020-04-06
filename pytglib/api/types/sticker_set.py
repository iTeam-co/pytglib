

from ..utils import Object


class StickerSet(Object):
    """
    Represents a sticker set

    Attributes:
        ID (:obj:`str`): ``StickerSet``

    Args:
        id (:obj:`int`):
            Identifier of the sticker set 
        title (:obj:`str`):
            Title of the sticker set 
        name (:obj:`str`):
            Name of the sticker set 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Sticker set thumbnail in WEBP format with width and height 100; may be nullThe file can be downloaded only before the thumbnail is changed
        is_installed (:obj:`bool`):
            True, if the sticker set has been installed by the current user 
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
        stickers (List of :class:`telegram.api.types.sticker`):
            List of stickers in this set 
        emojis (List of :class:`telegram.api.types.emojis`):
            A list of emoji corresponding to the stickers in the same orderThe list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerSet"

    def __init__(self, id, title, name, thumbnail, is_installed, is_archived, is_official, is_animated, is_masks, is_viewed, stickers, emojis, **kwargs):
        
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
        self.stickers = stickers  # list of sticker
        self.emojis = emojis  # list of emojis

    @staticmethod
    def read(q: dict, *args) -> "StickerSet":
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
        stickers = [Object.read(i) for i in q.get('stickers', [])]
        emojis = [Object.read(i) for i in q.get('emojis', [])]
        return StickerSet(id, title, name, thumbnail, is_installed, is_archived, is_official, is_animated, is_masks, is_viewed, stickers, emojis)
