

from ..utils import Object


class GetMessageThread(Object):
    """
    Returns information about a message thread. Can be used only if message.can_get_message_thread == true 

    Attributes:
        ID (:obj:`str`): ``GetMessageThread``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Identifier of the message

    Returns:
        MessageThreadInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageThread"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageThread":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessageThread(chat_id, message_id)
