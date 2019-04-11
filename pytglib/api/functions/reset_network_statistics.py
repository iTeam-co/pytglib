

from ..utils import Object


class ResetNetworkStatistics(Object):
    """
    Resets all network data usage statistics to zero. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``ResetNetworkStatistics``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetNetworkStatistics"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetNetworkStatistics":
        
        return ResetNetworkStatistics()
