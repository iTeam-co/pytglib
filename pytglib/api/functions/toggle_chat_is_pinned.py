

from ..utils import Object


class ToggleChatIsPinned(Object):
    """
    Changes the pinned state of a chat. You can pin up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") non-secret chats and the same number of secret chats in the main/archive chat list 

    Attributes:
        ID (:obj:`str`): ``ToggleChatIsPinned``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_pinned (:obj:`bool`):
            New value of is_pinned

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleChatIsPinned"

    def __init__(self, chat_id, is_pinned, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleChatIsPinned":
        chat_id = q.get('chat_id')
        is_pinned = q.get('is_pinned')
        return ToggleChatIsPinned(chat_id, is_pinned)
