

from ..utils import Object


class UpdateChatDefaultDisableNotification(Object):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatDefaultDisableNotification``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        default_disable_notification (:obj:`bool`):
            The new default_disable_notification value

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatDefaultDisableNotification"

    def __init__(self, chat_id, default_disable_notification, **kwargs):
        
        self.chat_id = chat_id  # int
        self.default_disable_notification = default_disable_notification  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatDefaultDisableNotification":
        chat_id = q.get('chat_id')
        default_disable_notification = q.get('default_disable_notification')
        return UpdateChatDefaultDisableNotification(chat_id, default_disable_notification)
