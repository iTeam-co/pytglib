

from ..utils import Object


class GetNetworkStatistics(Object):
    """
    Returns network data usage statistics. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetNetworkStatistics``

    Args:
        only_current (:obj:`bool`):
            If true, returns only data for the current library launch

    Returns:
        NetworkStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "getNetworkStatistics"

    def __init__(self, only_current, extra=None, **kwargs):
        self.extra = extra
        self.only_current = only_current  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetNetworkStatistics":
        only_current = q.get('only_current')
        return GetNetworkStatistics(only_current)
