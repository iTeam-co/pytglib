

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
        voice (:class:`telegram.api.types.file`):
            File containing the voice note

    Returns:
        VoiceNote

    Raises:
        :class:`telegram.Error`
    """
    ID = "voiceNote"

    def __init__(self, duration, waveform, mime_type, voice, **kwargs):
        
        self.duration = duration  # int
        self.waveform = waveform  # bytes
        self.mime_type = mime_type  # str
        self.voice = voice  # File

    @staticmethod
    def read(q: dict, *args) -> "VoiceNote":
        duration = q.get('duration')
        waveform = q.get('waveform')
        mime_type = q.get('mime_type')
        voice = Object.read(q.get('voice'))
        return VoiceNote(duration, waveform, mime_type, voice)
