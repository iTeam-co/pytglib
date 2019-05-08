

from ..utils import Object


class GetMessageLocally(Object):
    """
    Returns information about a message, if it is available locally without sending network request. This is an offline request 

    Attributes:
        ID (:obj:`str`): ``GetMessageLocally``

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
    ID = "getMessageLocally"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageLocally":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessageLocally(chat_id, message_id)
