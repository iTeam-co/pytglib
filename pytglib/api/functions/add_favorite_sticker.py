

from ..utils import Object


class AddFavoriteSticker(Object):
    """
    Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list

    Attributes:
        ID (:obj:`str`): ``AddFavoriteSticker``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker file to add

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addFavoriteSticker"

    def __init__(self, sticker, extra=None, **kwargs):
        self.extra = extra
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "AddFavoriteSticker":
        sticker = Object.read(q.get('sticker'))
        return AddFavoriteSticker(sticker)
