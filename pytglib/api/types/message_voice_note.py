

from ..utils import Object


class MessageVoiceNote(Object):
    """
    A voice note message 

    Attributes:
        ID (:obj:`str`): ``MessageVoiceNote``

    Args:
        voice_note (:class:`telegram.api.types.voiceNote`):
            The voice note description 
        caption (:class:`telegram.api.types.formattedText`):
            Voice note caption 
        is_listened (:obj:`bool`):
            True, if at least one of the recipients has listened to the voice note

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageVoiceNote"

    def __init__(self, voice_note, caption, is_listened, **kwargs):
        
        self.voice_note = voice_note  # VoiceNote
        self.caption = caption  # FormattedText
        self.is_listened = is_listened  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageVoiceNote":
        voice_note = Object.read(q.get('voice_note'))
        caption = Object.read(q.get('caption'))
        is_listened = q.get('is_listened')
        return MessageVoiceNote(voice_note, caption, is_listened)
