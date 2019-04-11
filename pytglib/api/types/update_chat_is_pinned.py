

from ..utils import Object


class UpdateChatIsPinned(Object):
    """
    A chat was pinned or unpinned 

    Attributes:
        ID (:obj:`str`): ``UpdateChatIsPinned``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_pinned (:obj:`bool`):
            New value of is_pinned 
        order (:obj:`int`):
            New value of the chat order

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatIsPinned"

    def __init__(self, chat_id, is_pinned, order, **kwargs):
        
        self.chat_id = chat_id  # int
        self.is_pinned = is_pinned  # bool
        self.order = order  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatIsPinned":
        chat_id = q.get('chat_id')
        is_pinned = q.get('is_pinned')
        order = q.get('order')
        return UpdateChatIsPinned(chat_id, is_pinned, order)
