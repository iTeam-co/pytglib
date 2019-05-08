

from ..utils import Object


class GetLogVerbosityLevel(Object):
    """
    Returns current verbosity level of the internal logging of TDLib. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``GetLogVerbosityLevel``

    No parameters required.

    Returns:
        LogVerbosityLevel

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLogVerbosityLevel"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetLogVerbosityLevel":
        
        return GetLogVerbosityLevel()
