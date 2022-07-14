

from ..utils import Object


class GetLogTagVerbosityLevel(Object):
    """
    Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetLogTagVerbosityLevel``

    Args:
        tag (:obj:`str`):
            Logging tag to change verbosity level

    Returns:
        LogVerbosityLevel

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLogTagVerbosityLevel"

    def __init__(self, tag, extra=None, **kwargs):
        self.extra = extra
        self.tag = tag  # str

    @staticmethod
    def read(q: dict, *args) -> "GetLogTagVerbosityLevel":
        tag = q.get('tag')
        return GetLogTagVerbosityLevel(tag)
