

from ..utils import Object


class GetImportedContactCount(Object):
    """
    Returns the total number of imported contacts

    Attributes:
        ID (:obj:`str`): ``GetImportedContactCount``

    No parameters required.

    Returns:
        Count

    Raises:
        :class:`telegram.Error`
    """
    ID = "getImportedContactCount"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetImportedContactCount":
        
        return GetImportedContactCount()
