

from ..utils import Object


class UpdateChatPosition(Object):
    """
    The position of a chat in a chat list has changed. Instead of this update updateChatLastMessage or updateChatDraftMessage might be sent 

    Attributes:
        ID (:obj:`str`): ``UpdateChatPosition``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        position (:class:`telegram.api.types.chatPosition`):
            New chat positionIf new order is 0, then the chat needs to be removed from the list

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatPosition"

    def __init__(self, chat_id, position, **kwargs):
        
        self.chat_id = chat_id  # int
        self.position = position  # ChatPosition

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatPosition":
        chat_id = q.get('chat_id')
        position = Object.read(q.get('position'))
        return UpdateChatPosition(chat_id, position)
