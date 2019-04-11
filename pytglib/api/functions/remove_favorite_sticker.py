

from ..utils import Object


class RemoveFavoriteSticker(Object):
    """
    Removes a sticker from the list of favorite stickers 

    Attributes:
        ID (:obj:`str`): ``RemoveFavoriteSticker``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker file to delete from the list

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeFavoriteSticker"

    def __init__(self, sticker, extra=None, **kwargs):
        self.extra = extra
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "RemoveFavoriteSticker":
        sticker = Object.read(q.get('sticker'))
        return RemoveFavoriteSticker(sticker)
