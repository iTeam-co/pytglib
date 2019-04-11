

from ..utils import Object


class AddRecentSticker(Object):
    """
    Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list

    Attributes:
        ID (:obj:`str`): ``AddRecentSticker``

    Args:
        is_attached (:obj:`bool`):
            Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers 
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker file to add

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "addRecentSticker"

    def __init__(self, is_attached, sticker, extra=None, **kwargs):
        self.extra = extra
        self.is_attached = is_attached  # bool
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "AddRecentSticker":
        is_attached = q.get('is_attached')
        sticker = Object.read(q.get('sticker'))
        return AddRecentSticker(is_attached, sticker)
