

from ..utils import Object


class UpdateChatPinnedMessage(Object):
    """
    The chat pinned message was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatPinnedMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        pinned_message_id (:obj:`int`):
            The new identifier of the pinned message; 0 if there is no pinned message in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatPinnedMessage"

    def __init__(self, chat_id, pinned_message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.pinned_message_id = pinned_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatPinnedMessage":
        chat_id = q.get('chat_id')
        pinned_message_id = q.get('pinned_message_id')
        return UpdateChatPinnedMessage(chat_id, pinned_message_id)
