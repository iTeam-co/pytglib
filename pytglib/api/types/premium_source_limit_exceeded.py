

from ..utils import Object


class PremiumSourceLimitExceeded(Object):
    """
    A limit was exceeded 

    Attributes:
        ID (:obj:`str`): ``PremiumSourceLimitExceeded``

    Args:
        limit_type (:class:`telegram.api.types.PremiumLimitType`):
            Type of the exceeded limit

    Returns:
        PremiumSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumSourceLimitExceeded"

    def __init__(self, limit_type, **kwargs):
        
        self.limit_type = limit_type  # PremiumLimitType

    @staticmethod
    def read(q: dict, *args) -> "PremiumSourceLimitExceeded":
        limit_type = Object.read(q.get('limit_type'))
        return PremiumSourceLimitExceeded(limit_type)
