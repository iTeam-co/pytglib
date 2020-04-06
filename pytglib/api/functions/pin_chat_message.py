

from ..utils import Object


class PinChatMessage(Object):
    """
    Pins a message in a chat; requires can_pin_messages rights 

    Attributes:
        ID (:obj:`str`): ``PinChatMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat 
        message_id (:obj:`int`):
            Identifier of the new pinned message 
        disable_notification (:obj:`bool`):
            True, if there should be no notification about the pinned message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "pinChatMessage"

    def __init__(self, chat_id, message_id, disable_notification, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.disable_notification = disable_notification  # bool

    @staticmethod
    def read(q: dict, *args) -> "PinChatMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        disable_notification = q.get('disable_notification')
        return PinChatMessage(chat_id, message_id, disable_notification)
