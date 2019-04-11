

from ..utils import Object


class GetMessages(Object):
    """
    Returns information about messages. If a message is not found, returns null on the corresponding position of the result 

    Attributes:
        ID (:obj:`str`): ``GetMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat the messages belong to 
        message_ids (List of :obj:`int`):
            Identifiers of the messages to get

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessages"

    def __init__(self, chat_id, message_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "GetMessages":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        return GetMessages(chat_id, message_ids)
