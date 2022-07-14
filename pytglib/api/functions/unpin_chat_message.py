

from ..utils import Object


class UnpinChatMessage(Object):
    """
    Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel 

    Attributes:
        ID (:obj:`str`): ``UnpinChatMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat 
        message_id (:obj:`int`):
            Identifier of the removed pinned message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "unpinChatMessage"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UnpinChatMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return UnpinChatMessage(chat_id, message_id)
