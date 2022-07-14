

from ..utils import Object


class PinChatMessage(Object):
    """
    Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel

    Attributes:
        ID (:obj:`str`): ``PinChatMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat
        message_id (:obj:`int`):
            Identifier of the new pinned message
        disable_notification (:obj:`bool`):
            Pass true to disable notification about the pinned messageNotifications are always disabled in channels and private chats
        only_for_self (:obj:`bool`):
            Pass true to pin the message only for self; private chats only

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "pinChatMessage"

    def __init__(self, chat_id, message_id, disable_notification, only_for_self, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.disable_notification = disable_notification  # bool
        self.only_for_self = only_for_self  # bool

    @staticmethod
    def read(q: dict, *args) -> "PinChatMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        disable_notification = q.get('disable_notification')
        only_for_self = q.get('only_for_self')
        return PinChatMessage(chat_id, message_id, disable_notification, only_for_self)
