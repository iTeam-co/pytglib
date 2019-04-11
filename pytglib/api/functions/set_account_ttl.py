

from ..utils import Object


class SetAccountTtl(Object):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted 

    Attributes:
        ID (:obj:`str`): ``SetAccountTtl``

    Args:
        ttl (:class:`telegram.api.types.accountTtl`):
            New account TTL

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setAccountTtl"

    def __init__(self, ttl, extra=None, **kwargs):
        self.extra = extra
        self.ttl = ttl  # AccountTtl

    @staticmethod
    def read(q: dict, *args) -> "SetAccountTtl":
        ttl = Object.read(q.get('ttl'))
        return SetAccountTtl(ttl)
