

from ..utils import Object


class Proxies(Object):
    """
    Represents a list of proxy servers 

    Attributes:
        ID (:obj:`str`): ``Proxies``

    Args:
        proxies (List of :class:`telegram.api.types.proxy`):
            List of proxy servers

    Returns:
        Proxies

    Raises:
        :class:`telegram.Error`
    """
    ID = "proxies"

    def __init__(self, proxies, **kwargs):
        
        self.proxies = proxies  # list of proxy

    @staticmethod
    def read(q: dict, *args) -> "Proxies":
        proxies = [Object.read(i) for i in q.get('proxies', [])]
        return Proxies(proxies)
