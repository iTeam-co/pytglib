

from ..utils import Object


class SetLogTagVerbosityLevel(Object):
    """
    Sets the verbosity level for a specified TDLib internal log tag. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``SetLogTagVerbosityLevel``

    Args:
        tag (:obj:`str`):
            Logging tag to change verbosity level 
        new_verbosity_level (:obj:`int`):
            New verbosity level; 1-1024

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setLogTagVerbosityLevel"

    def __init__(self, tag, new_verbosity_level, extra=None, **kwargs):
        self.extra = extra
        self.tag = tag  # str
        self.new_verbosity_level = new_verbosity_level  # int

    @staticmethod
    def read(q: dict, *args) -> "SetLogTagVerbosityLevel":
        tag = q.get('tag')
        new_verbosity_level = q.get('new_verbosity_level')
        return SetLogTagVerbosityLevel(tag, new_verbosity_level)
