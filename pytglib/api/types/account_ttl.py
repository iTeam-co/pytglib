

from ..utils import Object


class AccountTtl(Object):
    """
    Contains information about the period of inactivity after which the current user's account will automatically be deleted 

    Attributes:
        ID (:obj:`str`): ``AccountTtl``

    Args:
        days (:obj:`int`):
            Number of days of inactivity before the account will be flagged for deletion; should range from 30-366 days

    Returns:
        AccountTtl

    Raises:
        :class:`telegram.Error`
    """
    ID = "accountTtl"

    def __init__(self, days, **kwargs):
        
        self.days = days  # int

    @staticmethod
    def read(q: dict, *args) -> "AccountTtl":
        days = q.get('days')
        return AccountTtl(days)
