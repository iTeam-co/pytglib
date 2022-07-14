

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
        member_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the user or chat who performed the action 
        action (:class:`telegram.api.types.ChatEventAction`):
            The action

    Returns:
        ChatEvent

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEvent"

    def __init__(self, id, date, member_id, action, **kwargs):
        
        self.id = id  # int
        self.date = date  # int
        self.member_id = member_id  # MessageSender
        self.action = action  # ChatEventAction

    @staticmethod
    def read(q: dict, *args) -> "ChatEvent":
        id = q.get('id')
        date = q.get('date')
        member_id = Object.read(q.get('member_id'))
        action = Object.read(q.get('action'))
        return ChatEvent(id, date, member_id, action)
