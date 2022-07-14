

from ..utils import Object


class PremiumSource(Object):
    """
    Describes a source from which the Premium features screen is opened

    No parameters required.
    """
    ID = "premiumSource"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumSourceLink or PremiumSourceFeature or PremiumSourceLimitExceeded or PremiumSourceSettings":
        if q.get("@type"):
            return Object.read(q)
        return PremiumSource()
