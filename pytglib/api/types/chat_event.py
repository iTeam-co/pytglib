

from ..utils import Object


class ChatEvent(Object):
    """
    Represents a chat event 

    Attributes:
        ID (:obj:`str`): ``ChatEvent``

    Args:
        id (:obj:`int`):
            Chat event identifier 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the event happened 
        user_id (:obj:`int`):
            Identifier of the user who performed the action that triggered the event 
        action (:class:`telegram.api.types.ChatEventAction`):
            Action performed by the user

    Returns:
        ChatEvent

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEvent"

    def __init__(self, id, date, user_id, action, **kwargs):
        
        self.id = id  # int
        self.date = date  # int
        self.user_id = user_id  # int
        self.action = action  # ChatEventAction

    @staticmethod
    def read(q: dict, *args) -> "ChatEvent":
        id = q.get('id')
        date = q.get('date')
        user_id = q.get('user_id')
        action = Object.read(q.get('action'))
        return ChatEvent(id, date, user_id, action)
