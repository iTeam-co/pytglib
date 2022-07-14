

from ..utils import Object


class UnpinAllChatMessages(Object):
    """
    Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel 

    Attributes:
        ID (:obj:`str`): ``UnpinAllChatMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "unpinAllChatMessages"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UnpinAllChatMessages":
        chat_id = q.get('chat_id')
        return UnpinAllChatMessages(chat_id)
