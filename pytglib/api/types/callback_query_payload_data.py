

from ..utils import Object


class CallbackQueryPayloadData(Object):
    """
    The payload from a general callback button 

    Attributes:
        ID (:obj:`str`): ``CallbackQueryPayloadData``

    Args:
        data (:obj:`bytes`):
            Data that was attached to the callback button

    Returns:
        CallbackQueryPayload

    Raises:
        :class:`telegram.Error`
    """
    ID = "callbackQueryPayloadData"

    def __init__(self, data, **kwargs):
        
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "CallbackQueryPayloadData":
        data = q.get('data')
        return CallbackQueryPayloadData(data)
