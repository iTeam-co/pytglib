

from ..utils import Object


class ProcessDcUpdate(Object):
    """
    Handles a DC_UPDATE push service notification. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``ProcessDcUpdate``

    Args:
        dc (:obj:`str`):
            Value of the "dc" parameter of the notification 
        addr (:obj:`str`):
            Value of the "addr" parameter of the notification

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "processDcUpdate"

    def __init__(self, dc, addr, extra=None, **kwargs):
        self.extra = extra
        self.dc = dc  # str
        self.addr = addr  # str

    @staticmethod
    def read(q: dict, *args) -> "ProcessDcUpdate":
        dc = q.get('dc')
        addr = q.get('addr')
        return ProcessDcUpdate(dc, addr)
