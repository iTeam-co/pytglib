

from ..utils import Object


class UpdateChatLastMessage(Object):
    """
    The last message of a chat was changed. If last_message is null, then the last message in the chat became unknown. Some new unknown messages might be added to the chat in this case 

    Attributes:
        ID (:obj:`str`): ``UpdateChatLastMessage``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        last_message (:class:`telegram.api.types.message`):
            The new last message in the chat; may be null 
        order (:obj:`int`):
            New value of the chat order

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatLastMessage"

    def __init__(self, chat_id, last_message, order, **kwargs):
        
        self.chat_id = chat_id  # int
        self.last_message = last_message  # Message
        self.order = order  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatLastMessage":
        chat_id = q.get('chat_id')
        last_message = Object.read(q.get('last_message'))
        order = q.get('order')
        return UpdateChatLastMessage(chat_id, last_message, order)
