

from ..utils import Object


class GetFavoriteStickers(Object):
    """
    Returns favorite stickers

    Attributes:
        ID (:obj:`str`): ``GetFavoriteStickers``

    No parameters required.

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getFavoriteStickers"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetFavoriteStickers":
        
        return GetFavoriteStickers()
