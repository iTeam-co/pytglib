

from ..utils import Object


class VoiceNote(Object):
    """
    Describes a voice note. The voice note must be encoded with the Opus codec, and stored inside an OGG container. Voice notes can have only a single audio channel

    Attributes:
        ID (:obj:`str`): ``VoiceNote``

    Args:
        duration (:obj:`int`):
            Duration of the voice note, in seconds; as defined by the sender 
        waveform (:obj:`bytes`):
            A waveform representation of the voice note in 5-bit format
        mime_type (:obj:`str`):
            MIME type of the file; as defined by the sender 
        is_recognized (:obj:`bool`):
            True, if speech recognition is completed; Premium users only
        recognized_text (:obj:`str`):
            Recognized text of the voice note; Premium users onlyCall recognizeSpeech to get recognized text of the voice note 
        voice (:class:`telegram.api.types.file`):
            File containing the voice note

    Returns:
        VoiceNote

    Raises:
        :class:`telegram.Error`
    """
    ID = "voiceNote"

    def __init__(self, duration, waveform, mime_type, is_recognized, recognized_text, voice, **kwargs):
        
        self.duration = duration  # int
        self.waveform = waveform  # bytes
        self.mime_type = mime_type  # str
        self.is_recognized = is_recognized  # bool
        self.recognized_text = recognized_text  # str
        self.voice = voice  # File

    @staticmethod
    def read(q: dict, *args) -> "VoiceNote":
        duration = q.get('duration')
        waveform = q.get('waveform')
        mime_type = q.get('mime_type')
        is_recognized = q.get('is_recognized')
        recognized_text = q.get('recognized_text')
        voice = Object.read(q.get('voice'))
        return VoiceNote(duration, waveform, mime_type, is_recognized, recognized_text, voice)
