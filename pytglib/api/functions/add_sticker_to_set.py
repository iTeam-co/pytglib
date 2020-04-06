

from ..utils import Object


class AddStickerToSet(Object):
    """
    Adds a new sticker to a set; for bots only. Returns the sticker set

    Attributes:
        ID (:obj:`str`): ``AddStickerToSet``

    Args:
        user_id (:obj:`int`):
            Sticker set owner 
        name (:obj:`str`):
            Sticker set name 
        sticker (:class:`telegram.api.types.InputSticker`):
            Sticker to add to the set

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "addStickerToSet"

    def __init__(self, user_id, name, sticker, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.name = name  # str
        self.sticker = sticker  # InputSticker

    @staticmethod
    def read(q: dict, *args) -> "AddStickerToSet":
        user_id = q.get('user_id')
        name = q.get('name')
        sticker = Object.read(q.get('sticker'))
        return AddStickerToSet(user_id, name, sticker)
