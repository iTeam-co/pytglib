

from ..utils import Object


class CanPurchasePremium(Object):
    """
    Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase

    Attributes:
        ID (:obj:`str`): ``CanPurchasePremium``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "canPurchasePremium"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "CanPurchasePremium":
        
        return CanPurchasePremium()
