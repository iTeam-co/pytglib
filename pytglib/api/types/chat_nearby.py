

from ..utils import Object


class ChatNearby(Object):
    """
    Describes a chat located nearby 

    Attributes:
        ID (:obj:`str`): ``ChatNearby``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        distance (:obj:`int`):
            Distance to the chat location in meters

    Returns:
        ChatNearby

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatNearby"

    def __init__(self, chat_id, distance, **kwargs):
        
        self.chat_id = chat_id  # int
        self.distance = distance  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatNearby":
        chat_id = q.get('chat_id')
        distance = q.get('distance')
        return ChatNearby(chat_id, distance)
