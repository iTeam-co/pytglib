

from ..utils import Object


class MessageAudio(Object):
    """
    An audio message 

    Attributes:
        ID (:obj:`str`): ``MessageAudio``

    Args:
        audio (:class:`telegram.api.types.audio`):
            The audio description 
        caption (:class:`telegram.api.types.formattedText`):
            Audio caption

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageAudio"

    def __init__(self, audio, caption, **kwargs):
        
        self.audio = audio  # Audio
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "MessageAudio":
        audio = Object.read(q.get('audio'))
        caption = Object.read(q.get('caption'))
        return MessageAudio(audio, caption)
