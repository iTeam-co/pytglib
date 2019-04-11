

from ..utils import Object


class ChatEvents(Object):
    """
    Contains a list of chat events 

    Attributes:
        ID (:obj:`str`): ``ChatEvents``

    Args:
        events (List of :class:`telegram.api.types.chatEvent`):
            List of events

    Returns:
        ChatEvents

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEvents"

    def __init__(self, events, **kwargs):
        
        self.events = events  # list of chatEvent

    @staticmethod
    def read(q: dict, *args) -> "ChatEvents":
        events = [Object.read(i) for i in q.get('events', [])]
        return ChatEvents(events)
