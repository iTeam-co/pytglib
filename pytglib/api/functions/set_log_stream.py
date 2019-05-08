

from ..utils import Object


class SetLogStream(Object):
    """
    Sets new log stream for internal logging of TDLib. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``SetLogStream``

    Args:
        log_stream (:class:`telegram.api.types.LogStream`):
            New log stream

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setLogStream"

    def __init__(self, log_stream, extra=None, **kwargs):
        self.extra = extra
        self.log_stream = log_stream  # LogStream

    @staticmethod
    def read(q: dict, *args) -> "SetLogStream":
        log_stream = Object.read(q.get('log_stream'))
        return SetLogStream(log_stream)
