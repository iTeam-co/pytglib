

from ..utils import Object


class UnpinChatMessage(Object):
    """
    Removes the pinned message from a chat; requires can_pin_messages rights in the group or channel 

    Attributes:
        ID (:obj:`str`): ``UnpinChatMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "unpinChatMessage"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UnpinChatMessage":
        chat_id = q.get('chat_id')
        return UnpinChatMessage(chat_id)
