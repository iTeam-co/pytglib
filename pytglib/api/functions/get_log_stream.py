

from ..utils import Object


class GetLogStream(Object):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``GetLogStream``

    No parameters required.

    Returns:
        LogStream

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLogStream"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetLogStream":
        
        return GetLogStream()
