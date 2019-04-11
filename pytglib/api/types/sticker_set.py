

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
        is_installed (:obj:`bool`):
            True, if the sticker set has been installed by the current user
        is_archived (:obj:`bool`):
            True, if the sticker set has been archivedA sticker set can't be installed and archived simultaneously 
        is_official (:obj:`bool`):
            True, if the sticker set is official 
        is_masks (:obj:`bool`):
            True, if the stickers in the set are masks
        is_viewed (:obj:`bool`):
            True for already viewed trending sticker sets 
        stickers (List of :class:`telegram.api.types.sticker`):
            List of stickers in this set 
        emojis (List of :class:`telegram.api.types.stickerEmojis`):
            A list of emoji corresponding to the stickers in the same order

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "stickerSet"

    def __init__(self, id, title, name, is_installed, is_archived, is_official, is_masks, is_viewed, stickers, emojis, **kwargs):
        
        self.id = id  # int
        self.title = title  # str
        self.name = name  # str
        self.is_installed = is_installed  # bool
        self.is_archived = is_archived  # bool
        self.is_official = is_official  # bool
        self.is_masks = is_masks  # bool
        self.is_viewed = is_viewed  # bool
        self.stickers = stickers  # list of sticker
        self.emojis = emojis  # list of stickerEmojis

    @staticmethod
    def read(q: dict, *args) -> "StickerSet":
        id = q.get('id')
        title = q.get('title')
        name = q.get('name')
        is_installed = q.get('is_installed')
        is_archived = q.get('is_archived')
        is_official = q.get('is_official')
        is_masks = q.get('is_masks')
        is_viewed = q.get('is_viewed')
        stickers = [Object.read(i) for i in q.get('stickers', [])]
        emojis = [Object.read(i) for i in q.get('emojis', [])]
        return StickerSet(id, title, name, is_installed, is_archived, is_official, is_masks, is_viewed, stickers, emojis)
