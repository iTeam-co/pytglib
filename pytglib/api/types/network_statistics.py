

from ..utils import Object


class NetworkStatistics(Object):
    """
    A full list of available network statistic entries 

    Attributes:
        ID (:obj:`str`): ``NetworkStatistics``

    Args:
        since_date (:obj:`int`):
            Point in time (Unix timestamp) when the app began collecting statistics 
        entries (List of :class:`telegram.api.types.NetworkStatisticsEntry`):
            Network statistics entries

    Returns:
        NetworkStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "networkStatistics"

    def __init__(self, since_date, entries, **kwargs):
        
        self.since_date = since_date  # int
        self.entries = entries  # list of NetworkStatisticsEntry

    @staticmethod
    def read(q: dict, *args) -> "NetworkStatistics":
        since_date = q.get('since_date')
        entries = [Object.read(i) for i in q.get('entries', [])]
        return NetworkStatistics(since_date, entries)
