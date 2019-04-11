

from ..utils import Object


class GetProxies(Object):
    """
    Returns list of proxies that are currently set up. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetProxies``

    No parameters required.

    Returns:
        Proxies

    Raises:
        :class:`telegram.Error`
    """
    ID = "getProxies"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetProxies":
        
        return GetProxies()
