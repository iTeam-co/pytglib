

from ..utils import Object


class AddNetworkStatistics(Object):
    """
    Adds the specified data to data usage statistics. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``AddNetworkStatistics``

    Args:
        entry (:class:`telegram.api.types.NetworkStatisticsEntry`):
            The network statistics entry with the data to be added to statistics

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addNetworkStatistics"

    def __init__(self, entry, extra=None, **kwargs):
        self.extra = extra
        self.entry = entry  # NetworkStatisticsEntry

    @staticmethod
    def read(q: dict, *args) -> "AddNetworkStatistics":
        entry = Object.read(q.get('entry'))
        return AddNetworkStatistics(entry)
