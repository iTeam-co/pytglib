

from ..utils import Object


class GetPremiumStickers(Object):
    """
    Returns examples of premium stickers for demonstration purposes

    Attributes:
        ID (:obj:`str`): ``GetPremiumStickers``

    No parameters required.

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPremiumStickers"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetPremiumStickers":
        
        return GetPremiumStickers()
