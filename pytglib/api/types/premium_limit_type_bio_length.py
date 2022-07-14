

from ..utils import Object


class PremiumLimitTypeBioLength(Object):
    """
    The maximum length of the user's bio

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeBioLength``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeBioLength"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeBioLength":
        
        return PremiumLimitTypeBioLength()
