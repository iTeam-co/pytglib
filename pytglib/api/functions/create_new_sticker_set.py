

from ..utils import Object


class CreateNewStickerSet(Object):
    """
    Creates a new sticker set. Returns the newly created sticker set

    Attributes:
        ID (:obj:`str`): ``CreateNewStickerSet``

    Args:
        user_id (:obj:`int`):
            Sticker set owner; ignored for regular users
        title (:obj:`str`):
            Sticker set title; 1-64 characters
        name (:obj:`str`):
            Sticker set nameCan contain only English letters, digits and underscoresMust end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters
        stickers (List of :class:`telegram.api.types.inputSticker`):
            List of stickers to be added to the set; must be non-emptyAll stickers must have the same formatFor TGS stickers, uploadStickerFile must be used before the sticker is shown
        source (:obj:`str`):
            Source of the sticker set; may be empty if unknown

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewStickerSet"

    def __init__(self, user_id, title, name, stickers, source, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.title = title  # str
        self.name = name  # str
        self.stickers = stickers  # list of inputSticker
        self.source = source  # str

    @staticmethod
    def read(q: dict, *args) -> "CreateNewStickerSet":
        user_id = q.get('user_id')
        title = q.get('title')
        name = q.get('name')
        stickers = [Object.read(i) for i in q.get('stickers', [])]
        source = q.get('source')
        return CreateNewStickerSet(user_id, title, name, stickers, source)
