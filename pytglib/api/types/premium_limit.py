

from ..utils import Object


class PremiumLimit(Object):
    """
    Contains information about a limit, increased for Premium users 

    Attributes:
        ID (:obj:`str`): ``PremiumLimit``

    Args:
        type (:class:`telegram.api.types.PremiumLimitType`):
            The type of the limit 
        default_value (:obj:`int`):
            Default value of the limit 
        premium_value (:obj:`int`):
            Value of the limit for Premium users

    Returns:
        PremiumLimit

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumLimit"

    def __init__(self, type, default_value, premium_value, **kwargs):
        
        self.type = type  # PremiumLimitType
        self.default_value = default_value  # int
        self.premium_value = premium_value  # int

    @staticmethod
    def read(q: dict, *args) -> "PremiumLimit":
        type = Object.read(q.get('type'))
        default_value = q.get('default_value')
        premium_value = q.get('premium_value')
        return PremiumLimit(type, default_value, premium_value)
