

from ..utils import Object


class UpdateChatOrder(Object):
    """
    The order of the chat in the chat list has changed. Instead of this update updateChatLastMessage, updateChatIsPinned, updateChatDraftMessage, or updateChatIsSponsored might be sent 

    Attributes:
        ID (:obj:`str`): ``UpdateChatOrder``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        order (:obj:`int`):
            New value of the order

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatOrder"

    def __init__(self, chat_id, order, **kwargs):
        
        self.chat_id = chat_id  # int
        self.order = order  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatOrder":
        chat_id = q.get('chat_id')
        order = q.get('order')
        return UpdateChatOrder(chat_id, order)
