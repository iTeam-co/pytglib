

from ..utils import Object


class GetPremiumState(Object):
    """
    Returns state of Telegram Premium subscription and promotion videos for Premium features

    Attributes:
        ID (:obj:`str`): ``GetPremiumState``

    No parameters required.

    Returns:
        PremiumState

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPremiumState"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetPremiumState":
        
        return GetPremiumState()
