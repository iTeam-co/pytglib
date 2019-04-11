

from ..utils import Object


class SendChatAction(Object):
    """
    Sends a notification about user activity in a chat 

    Attributes:
        ID (:obj:`str`): ``SendChatAction``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        action (:class:`telegram.api.types.ChatAction`):
            The action description

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendChatAction"

    def __init__(self, chat_id, action, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.action = action  # ChatAction

    @staticmethod
    def read(q: dict, *args) -> "SendChatAction":
        chat_id = q.get('chat_id')
        action = Object.read(q.get('action'))
        return SendChatAction(chat_id, action)
