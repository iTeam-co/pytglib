

from ..utils import Object


class SaveApplicationLogEvent(Object):
    """
    Saves application log event on the server. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``SaveApplicationLogEvent``

    Args:
        type (:obj:`str`):
            Event type 
        chat_id (:obj:`int`):
            Optional chat identifier, associated with the event 
        data (:class:`telegram.api.types.JsonValue`):
            The log event data

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "saveApplicationLogEvent"

    def __init__(self, type, chat_id, data, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # str
        self.chat_id = chat_id  # int
        self.data = data  # JsonValue

    @staticmethod
    def read(q: dict, *args) -> "SaveApplicationLogEvent":
        type = q.get('type')
        chat_id = q.get('chat_id')
        data = Object.read(q.get('data'))
        return SaveApplicationLogEvent(type, chat_id, data)
