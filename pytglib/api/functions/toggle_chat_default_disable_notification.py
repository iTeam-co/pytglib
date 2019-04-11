

from ..utils import Object


class ToggleChatDefaultDisableNotification(Object):
    """
    Changes the value of the default disable_notification parameter, used when a message is sent to a chat 

    Attributes:
        ID (:obj:`str`): ``ToggleChatDefaultDisableNotification``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        default_disable_notification (:obj:`bool`):
            New value of default_disable_notification

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleChatDefaultDisableNotification"

    def __init__(self, chat_id, default_disable_notification, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.default_disable_notification = default_disable_notification  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleChatDefaultDisableNotification":
        chat_id = q.get('chat_id')
        default_disable_notification = q.get('default_disable_notification')
        return ToggleChatDefaultDisableNotification(chat_id, default_disable_notification)
