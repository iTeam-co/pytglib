

from ..utils import Object


class PushMessageContentAudio(Object):
    """
    An audio message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentAudio``

    Args:
        audio (:class:`telegram.api.types.audio`):
            Message content; may be null 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentAudio"

    def __init__(self, audio, is_pinned, **kwargs):
        
        self.audio = audio  # Audio
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentAudio":
        audio = Object.read(q.get('audio'))
        is_pinned = q.get('is_pinned')
        return PushMessageContentAudio(audio, is_pinned)
