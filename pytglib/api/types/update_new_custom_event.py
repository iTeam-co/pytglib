

from ..utils import Object


class UpdateNewCustomEvent(Object):
    """
    A new incoming event; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewCustomEvent``

    Args:
        event (:obj:`str`):
            A JSON-serialized event

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewCustomEvent"

    def __init__(self, event, **kwargs):
        
        self.event = event  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewCustomEvent":
        event = q.get('event')
        return UpdateNewCustomEvent(event)
