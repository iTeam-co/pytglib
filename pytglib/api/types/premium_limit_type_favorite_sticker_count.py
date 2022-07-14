

from ..utils import Object


class PremiumLimitTypeFavoriteStickerCount(Object):
    """
    The maximum number of favorite stickers

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeFavoriteStickerCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeFavoriteStickerCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeFavoriteStickerCount":
        
        return PremiumLimitTypeFavoriteStickerCount()
