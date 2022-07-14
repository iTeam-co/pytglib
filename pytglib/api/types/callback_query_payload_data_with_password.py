

from ..utils import Object


class CallbackQueryPayloadDataWithPassword(Object):
    """
    The payload for a callback button requiring password 

    Attributes:
        ID (:obj:`str`): ``CallbackQueryPayloadDataWithPassword``

    Args:
        password (:obj:`str`):
            The password for the current user 
        data (:obj:`bytes`):
            Data that was attached to the callback button

    Returns:
        CallbackQueryPayload

    Raises:
        :class:`telegram.Error`
    """
    ID = "callbackQueryPayloadDataWithPassword"

    def __init__(self, password, data, **kwargs):
        
        self.password = password  # str
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "CallbackQueryPayloadDataWithPassword":
        password = q.get('password')
        data = q.get('data')
        return CallbackQueryPayloadDataWithPassword(password, data)
