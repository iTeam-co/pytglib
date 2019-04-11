

from ..utils import Object


class InputMessageVoiceNote(Object):
    """
    A voice note message 

    Attributes:
        ID (:obj:`str`): ``InputMessageVoiceNote``

    Args:
        voice_note (:class:`telegram.api.types.InputFile`):
            Voice note to be sent 
        duration (:obj:`int`):
            Duration of the voice note, in seconds 
        waveform (:obj:`bytes`):
            Waveform representation of the voice note, in 5-bit format 
        caption (:class:`telegram.api.types.formattedText`):
            Voice note caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageVoiceNote"

    def __init__(self, voice_note, duration, waveform, caption, **kwargs):
        
        self.voice_note = voice_note  # InputFile
        self.duration = duration  # int
        self.waveform = waveform  # bytes
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageVoiceNote":
        voice_note = Object.read(q.get('voice_note'))
        duration = q.get('duration')
        waveform = q.get('waveform')
        caption = Object.read(q.get('caption'))
        return InputMessageVoiceNote(voice_note, duration, waveform, caption)
