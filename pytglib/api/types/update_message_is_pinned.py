

from ..utils import Object


class UpdateMessageIsPinned(Object):
    """
    The message pinned state was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageIsPinned``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            The message identifier 
        is_pinned (:obj:`bool`):
            True, if the message is pinned

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageIsPinned"

    def __init__(self, chat_id, message_id, is_pinned, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageIsPinned":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        is_pinned = q.get('is_pinned')
        return UpdateMessageIsPinned(chat_id, message_id, is_pinned)
