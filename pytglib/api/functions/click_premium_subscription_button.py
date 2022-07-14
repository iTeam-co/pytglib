

from ..utils import Object


class ClickPremiumSubscriptionButton(Object):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen

    Attributes:
        ID (:obj:`str`): ``ClickPremiumSubscriptionButton``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "clickPremiumSubscriptionButton"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ClickPremiumSubscriptionButton":
        
        return ClickPremiumSubscriptionButton()
