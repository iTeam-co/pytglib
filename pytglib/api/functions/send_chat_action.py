

from ..utils import Object


class SendChatAction(Object):
    """
    Sends a notification about user activity in a chat 

    Attributes:
        ID (:obj:`str`): ``SendChatAction``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_thread_id (:obj:`int`):
            If not 0, a message thread identifier in which the action was performed 
        action (:class:`telegram.api.types.ChatAction`):
            The action description; pass null to cancel the currently active action

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendChatAction"

    def __init__(self, chat_id, message_thread_id, action, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.action = action  # ChatAction

    @staticmethod
    def read(q: dict, *args) -> "SendChatAction":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        action = Object.read(q.get('action'))
        return SendChatAction(chat_id, message_thread_id, action)
