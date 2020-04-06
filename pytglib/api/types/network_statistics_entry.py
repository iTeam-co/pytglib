

from ..utils import Object


class NetworkStatisticsEntry(Object):
    """
    Contains statistics about network usage

    No parameters required.
    """
    ID = "networkStatisticsEntry"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "NetworkStatisticsEntryFile or NetworkStatisticsEntryCall":
        if q.get("@type"):
            return Object.read(q)
        return NetworkStatisticsEntry()
