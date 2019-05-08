

from ..utils import Object


class LogStreamEmpty(Object):
    """
    The log is written nowhere

    Attributes:
        ID (:obj:`str`): ``LogStreamEmpty``

    No parameters required.

    Returns:
        LogStream

    Raises:
        :class:`telegram.Error`
    """
    ID = "logStreamEmpty"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LogStreamEmpty":
        
        return LogStreamEmpty()
