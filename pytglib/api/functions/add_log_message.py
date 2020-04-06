

from ..utils import Object


class AddLogMessage(Object):
    """
    Adds a message to TDLib internal log. This is an offline method. Can be called before authorization. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``AddLogMessage``

    Args:
        verbosity_level (:obj:`int`):
            The minimum verbosity level needed for the message to be logged, 0-1023 
        text (:obj:`str`):
            Text of a message to log

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addLogMessage"

    def __init__(self, verbosity_level, text, extra=None, **kwargs):
        self.extra = extra
        self.verbosity_level = verbosity_level  # int
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "AddLogMessage":
        verbosity_level = q.get('verbosity_level')
        text = q.get('text')
        return AddLogMessage(verbosity_level, text)
