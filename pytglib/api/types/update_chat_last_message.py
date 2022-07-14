

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
        positions (List of :class:`telegram.api.types.chatPosition`):
            The new chat positions in the chat lists

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatLastMessage"

    def __init__(self, chat_id, last_message, positions, **kwargs):
        
        self.chat_id = chat_id  # int
        self.last_message = last_message  # Message
        self.positions = positions  # list of chatPosition

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatLastMessage":
        chat_id = q.get('chat_id')
        last_message = Object.read(q.get('last_message'))
        positions = [Object.read(i) for i in q.get('positions', [])]
        return UpdateChatLastMessage(chat_id, last_message, positions)
