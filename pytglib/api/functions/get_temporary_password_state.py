

from ..utils import Object


class GetTemporaryPasswordState(Object):
    """
    Returns information about the current temporary password

    Attributes:
        ID (:obj:`str`): ``GetTemporaryPasswordState``

    No parameters required.

    Returns:
        TemporaryPasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "getTemporaryPasswordState"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetTemporaryPasswordState":
        
        return GetTemporaryPasswordState()
