

from ..utils import Object


class GetAccountTtl(Object):
    """
    Returns the period of inactivity after which the account of the current user will automatically be deleted

    Attributes:
        ID (:obj:`str`): ``GetAccountTtl``

    No parameters required.

    Returns:
        AccountTtl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAccountTtl"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetAccountTtl":
        
        return GetAccountTtl()
