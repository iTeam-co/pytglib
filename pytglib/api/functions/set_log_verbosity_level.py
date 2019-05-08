

from ..utils import Object


class SetLogVerbosityLevel(Object):
    """
    Sets the verbosity level of the internal logging of TDLib. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``SetLogVerbosityLevel``

    Args:
        new_verbosity_level (:obj:`int`):
            New value of the verbosity level for loggingValue 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setLogVerbosityLevel"

    def __init__(self, new_verbosity_level, extra=None, **kwargs):
        self.extra = extra
        self.new_verbosity_level = new_verbosity_level  # int

    @staticmethod
    def read(q: dict, *args) -> "SetLogVerbosityLevel":
        new_verbosity_level = q.get('new_verbosity_level')
        return SetLogVerbosityLevel(new_verbosity_level)
