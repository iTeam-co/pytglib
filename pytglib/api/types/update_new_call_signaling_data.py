

from ..utils import Object


class UpdateNewCallSignalingData(Object):
    """
    New call signaling data arrived 

    Attributes:
        ID (:obj:`str`): ``UpdateNewCallSignalingData``

    Args:
        call_id (:obj:`int`):
            The call identifier 
        data (:obj:`bytes`):
            The data

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewCallSignalingData"

    def __init__(self, call_id, data, **kwargs):
        
        self.call_id = call_id  # int
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewCallSignalingData":
        call_id = q.get('call_id')
        data = q.get('data')
        return UpdateNewCallSignalingData(call_id, data)
