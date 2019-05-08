

from ..utils import Object


class GetStorageStatisticsFast(Object):
    """
    Quickly returns approximate storage usage statistics. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetStorageStatisticsFast``

    No parameters required.

    Returns:
        StorageStatisticsFast

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStorageStatisticsFast"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetStorageStatisticsFast":
        
        return GetStorageStatisticsFast()
