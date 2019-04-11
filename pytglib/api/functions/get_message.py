

from ..utils import Object


class GetMessage(Object):
    """
    Returns information about a message 

    Attributes:
        ID (:obj:`str`): ``GetMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message to get

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessage"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessage(chat_id, message_id)
