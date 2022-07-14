

from ..utils import Object


class MessageCall(Object):
    """
    A message with information about an ended call 

    Attributes:
        ID (:obj:`str`): ``MessageCall``

    Args:
        is_video (:obj:`bool`):
            True, if the call was a video call 
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

    def __init__(self, is_video, discard_reason, duration, **kwargs):
        
        self.is_video = is_video  # bool
        self.discard_reason = discard_reason  # CallDiscardReason
        self.duration = duration  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageCall":
        is_video = q.get('is_video')
        discard_reason = Object.read(q.get('discard_reason'))
        duration = q.get('duration')
        return MessageCall(is_video, discard_reason, duration)
