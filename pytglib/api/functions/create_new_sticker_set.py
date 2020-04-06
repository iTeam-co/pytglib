

from ..utils import Object


class CreateNewStickerSet(Object):
    """
    Creates a new sticker set; for bots only. Returns the newly created sticker set

    Attributes:
        ID (:obj:`str`): ``CreateNewStickerSet``

    Args:
        user_id (:obj:`int`):
            Sticker set owner
        title (:obj:`str`):
            Sticker set title; 1-64 characters
        name (:obj:`str`):
            Sticker set nameCan contain only English letters, digits and underscoresMust end with *"_by_<bot username>"* (*<bot_username>* is case insensitive); 1-64 characters
        is_masks (:obj:`bool`):
            True, if stickers are masksAnimated stickers can't be masks
        stickers (List of :class:`telegram.api.types.InputSticker`):
            List of stickers to be added to the set; must be non-emptyAll stickers must be of the same type

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewStickerSet"

    def __init__(self, user_id, title, name, is_masks, stickers, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.title = title  # str
        self.name = name  # str
        self.is_masks = is_masks  # bool
        self.stickers = stickers  # list of InputSticker

    @staticmethod
    def read(q: dict, *args) -> "CreateNewStickerSet":
        user_id = q.get('user_id')
        title = q.get('title')
        name = q.get('name')
        is_masks = q.get('is_masks')
        stickers = [Object.read(i) for i in q.get('stickers', [])]
        return CreateNewStickerSet(user_id, title, name, is_masks, stickers)
