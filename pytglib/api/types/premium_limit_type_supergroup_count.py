

from ..utils import Object


class PremiumLimitTypeSupergroupCount(Object):
    """
    The maximum number of joined supergroups and channels

    Attributes:
        ID (:obj:`str`): ``PremiumLimitTypeSupergroupCount``

    No parameters required.

    Returns:
        PremiumLimitType

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimitTypeSupergroupCount"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimitTypeSupergroupCount":
        
        return PremiumLimitTypeSupergroupCount()
