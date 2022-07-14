

from ..utils import Object


class SendCallSignalingData(Object):
    """
    Sends call signaling data 

    Attributes:
        ID (:obj:`str`): ``SendCallSignalingData``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        data (:obj:`bytes`):
            The data

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCallSignalingData"

    def __init__(self, call_id, data, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "SendCallSignalingData":
        call_id = q.get('call_id')
        data = q.get('data')
        return SendCallSignalingData(call_id, data)
