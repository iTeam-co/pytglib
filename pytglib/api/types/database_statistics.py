

from ..utils import Object


class DatabaseStatistics(Object):
    """
    Contains database statistics

    Attributes:
        ID (:obj:`str`): ``DatabaseStatistics``

    Args:
        statistics (:obj:`str`):
            Database statistics in an unspecified human-readable format

    Returns:
        DatabaseStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "databaseStatistics"

    def __init__(self, statistics, **kwargs):
        
        self.statistics = statistics  # str

    @staticmethod
    def read(q: dict, *args) -> "DatabaseStatistics":
        statistics = q.get('statistics')
        return DatabaseStatistics(statistics)
