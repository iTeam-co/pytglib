

from ..utils import Object


class SendCallDebugInformation(Object):
    """
    Sends debug information for a call 

    Attributes:
        ID (:obj:`str`): ``SendCallDebugInformation``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        debug_information (:obj:`str`):
            Debug information in application-specific format

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCallDebugInformation"

    def __init__(self, call_id, debug_information, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.debug_information = debug_information  # str

    @staticmethod
    def read(q: dict, *args) -> "SendCallDebugInformation":
        call_id = q.get('call_id')
        debug_information = q.get('debug_information')
        return SendCallDebugInformation(call_id, debug_information)
