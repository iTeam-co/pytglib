

from ..utils import Object


class PremiumSourceSettings(Object):
    """
    A user opened the Premium features screen from settings

    Attributes:
        ID (:obj:`str`): ``PremiumSourceSettings``

    No parameters required.

    Returns:
        PremiumSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumSourceSettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumSourceSettings":
        
        return PremiumSourceSettings()
