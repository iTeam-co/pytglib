

from ..utils import Object


class MessageCall(Object):
    """
    A message with information about an ended call 

    Attributes:
        ID (:obj:`str`): ``MessageCall``

    Args:
        discard_reason (:class:`telegram.api.types.CallDiscardReason`):
            Reason why the call was discarded 
        duration (:obj:`int`):
            Call duration, in seconds

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageCall"

    def __init__(self, discard_reason, duration, **kwargs):
        
        self.discard_reason = discard_reason  # CallDiscardReason
        self.duration = duration  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageCall":
        discard_reason = Object.read(q.get('discard_reason'))
        duration = q.get('duration')
        return MessageCall(discard_reason, duration)
