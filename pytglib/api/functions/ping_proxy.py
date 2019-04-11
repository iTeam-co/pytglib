

from ..utils import Object


class PingProxy(Object):
    """
    Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``PingProxy``

    Args:
        proxy_id (:obj:`int`):
            Proxy identifierUse 0 to ping a Telegram server without a proxy

    Returns:
        Seconds

    Raises:
        :class:`telegram.Error`
    """
    ID = "pingProxy"

    def __init__(self, proxy_id, extra=None, **kwargs):
        self.extra = extra
        self.proxy_id = proxy_id  # int

    @staticmethod
    def read(q: dict, *args) -> "PingProxy":
        proxy_id = q.get('proxy_id')
        return PingProxy(proxy_id)
