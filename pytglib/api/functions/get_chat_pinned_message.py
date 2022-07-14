

from ..utils import Object


class GetChatPinnedMessage(Object):
    """
    Returns information about a newest pinned message in the chat 

    Attributes:
        ID (:obj:`str`): ``GetChatPinnedMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat the message belongs to

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatPinnedMessage"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatPinnedMessage":
        chat_id = q.get('chat_id')
        return GetChatPinnedMessage(chat_id)
