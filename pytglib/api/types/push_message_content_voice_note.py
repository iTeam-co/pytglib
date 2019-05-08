

from ..utils import Object


class PushMessageContentVoiceNote(Object):
    """
    A voice note message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentVoiceNote``

    Args:
        voice_note (:class:`telegram.api.types.voiceNote`):
            Message content; may be null 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentVoiceNote"

    def __init__(self, voice_note, is_pinned, **kwargs):
        
        self.voice_note = voice_note  # VoiceNote
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentVoiceNote":
        voice_note = Object.read(q.get('voice_note'))
        is_pinned = q.get('is_pinned')
        return PushMessageContentVoiceNote(voice_note, is_pinned)
