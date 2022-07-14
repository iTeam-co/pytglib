

from ..utils import Object


class GetChatAvailableMessageSenders(Object):
    """
    Returns list of message sender identifiers, which can be used to send messages in a chat 

    Attributes:
        ID (:obj:`str`): ``GetChatAvailableMessageSenders``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        MessageSenders

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatAvailableMessageSenders"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatAvailableMessageSenders":
        chat_id = q.get('chat_id')
        return GetChatAvailableMessageSenders(chat_id)
