

from ..utils import Object


class GetDatabaseStatistics(Object):
    """
    Returns database statistics

    Attributes:
        ID (:obj:`str`): ``GetDatabaseStatistics``

    No parameters required.

    Returns:
        DatabaseStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "getDatabaseStatistics"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetDatabaseStatistics":
        
        return GetDatabaseStatistics()
