

from ..utils import Object


class SendChatScreenshotTakenNotification(Object):
    """
    Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats 

    Attributes:
        ID (:obj:`str`): ``SendChatScreenshotTakenNotification``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendChatScreenshotTakenNotification"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SendChatScreenshotTakenNotification":
        chat_id = q.get('chat_id')
        return SendChatScreenshotTakenNotification(chat_id)
