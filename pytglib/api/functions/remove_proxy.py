

from ..utils import Object


class RemoveProxy(Object):
    """
    Removes a proxy server. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``RemoveProxy``

    Args:
        proxy_id (:obj:`int`):
            Proxy identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeProxy"

    def __init__(self, proxy_id, extra=None, **kwargs):
        self.extra = extra
        self.proxy_id = proxy_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveProxy":
        proxy_id = q.get('proxy_id')
        return RemoveProxy(proxy_id)
