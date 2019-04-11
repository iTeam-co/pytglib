

from ..utils import Object


class UpdateFavoriteStickers(Object):
    """
    The list of favorite stickers was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateFavoriteStickers``

    Args:
        sticker_ids (List of :obj:`int`):
            The new list of file identifiers of favorite stickers

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFavoriteStickers"

    def __init__(self, sticker_ids, **kwargs):
        
        self.sticker_ids = sticker_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateFavoriteStickers":
        sticker_ids = q.get('sticker_ids')
        return UpdateFavoriteStickers(sticker_ids)
