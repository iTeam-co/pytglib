

from ..utils import Object


class EnableProxy(Object):
    """
    Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``EnableProxy``

    Args:
        proxy_id (:obj:`int`):
            Proxy identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "enableProxy"

    def __init__(self, proxy_id, extra=None, **kwargs):
        self.extra = extra
        self.proxy_id = proxy_id  # int

    @staticmethod
    def read(q: dict, *args) -> "EnableProxy":
        proxy_id = q.get('proxy_id')
        return EnableProxy(proxy_id)
