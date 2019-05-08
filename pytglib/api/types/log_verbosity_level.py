

from ..utils import Object


class LogVerbosityLevel(Object):
    """
    Contains a TDLib internal log verbosity level 

    Attributes:
        ID (:obj:`str`): ``LogVerbosityLevel``

    Args:
        verbosity_level (:obj:`int`):
            Log verbosity level

    Returns:
        LogVerbosityLevel

    Raises:
        :class:`telegram.Error`
    """
    ID = "logVerbosityLevel"

    def __init__(self, verbosity_level, **kwargs):
        
        self.verbosity_level = verbosity_level  # int

    @staticmethod
    def read(q: dict, *args) -> "LogVerbosityLevel":
        verbosity_level = q.get('verbosity_level')
        return LogVerbosityLevel(verbosity_level)
