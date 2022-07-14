

from ..utils import Object


class GetPremiumLimit(Object):
    """
    Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown 

    Attributes:
        ID (:obj:`str`): ``GetPremiumLimit``

    Args:
        limit_type (:class:`telegram.api.types.PremiumLimitType`):
            Type of the limit

    Returns:
        PremiumLimit

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPremiumLimit"

    def __init__(self, limit_type, extra=None, **kwargs):
        self.extra = extra
        self.limit_type = limit_type  # PremiumLimitType

    @staticmethod
    def read(q: dict, *args) -> "GetPremiumLimit":
        limit_type = Object.read(q.get('limit_type'))
        return GetPremiumLimit(limit_type)
