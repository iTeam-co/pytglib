

from ..utils import Object


class LogStreamDefault(Object):
    """
    The log is written to stderr or an OS specific log

    Attributes:
        ID (:obj:`str`): ``LogStreamDefault``

    No parameters required.

    Returns:
        LogStream

    Raises:
        :class:`telegram.Error`
    """
    ID = "logStreamDefault"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LogStreamDefault":
        
        return LogStreamDefault()
