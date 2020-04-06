

from ..utils import Object


class ChatEventLocationChanged(Object):
    """
    The supergroup location was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventLocationChanged``

    Args:
        old_location (:class:`telegram.api.types.chatLocation`):
            Previous location; may be null 
        new_location (:class:`telegram.api.types.chatLocation`):
            New location; may be null

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventLocationChanged"

    def __init__(self, old_location, new_location, **kwargs):
        
        self.old_location = old_location  # ChatLocation
        self.new_location = new_location  # ChatLocation

    @staticmethod
    def read(q: dict, *args) -> "ChatEventLocationChanged":
        old_location = Object.read(q.get('old_location'))
        new_location = Object.read(q.get('new_location'))
        return ChatEventLocationChanged(old_location, new_location)
