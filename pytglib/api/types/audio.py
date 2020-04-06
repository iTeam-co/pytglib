

from ..utils import Object


class Audio(Object):
    """
    Describes an audio file. Audio is usually in MP3 or M4A format 

    Attributes:
        ID (:obj:`str`): ``Audio``

    Args:
        duration (:obj:`int`):
            Duration of the audio, in seconds; as defined by the sender 
        title (:obj:`str`):
            Title of the audio; as defined by the sender 
        performer (:obj:`str`):
            Performer of the audio; as defined by the sender
        file_name (:obj:`str`):
            Original name of the file; as defined by the sender 
        mime_type (:obj:`str`):
            The MIME type of the file; as defined by the sender 
        album_cover_minithumbnail (:class:`telegram.api.types.minithumbnail`):
            The minithumbnail of the album cover; may be null 
        album_cover_thumbnail (:class:`telegram.api.types.photoSize`):
            The thumbnail of the album cover; as defined by the senderThe full size thumbnail should be extracted from the downloaded file; may be null 
        audio (:class:`telegram.api.types.file`):
            File containing the audio

    Returns:
        Audio

    Raises:
        :class:`telegram.Error`
    """
    ID = "audio"

    def __init__(self, duration, title, performer, file_name, mime_type, album_cover_minithumbnail, album_cover_thumbnail, audio, **kwargs):
        
        self.duration = duration  # int
        self.title = title  # str
        self.performer = performer  # str
        self.file_name = file_name  # str
        self.mime_type = mime_type  # str
        self.album_cover_minithumbnail = album_cover_minithumbnail  # Minithumbnail
        self.album_cover_thumbnail = album_cover_thumbnail  # PhotoSize
        self.audio = audio  # File

    @staticmethod
    def read(q: dict, *args) -> "Audio":
        duration = q.get('duration')
        title = q.get('title')
        performer = q.get('performer')
        file_name = q.get('file_name')
        mime_type = q.get('mime_type')
        album_cover_minithumbnail = Object.read(q.get('album_cover_minithumbnail'))
        album_cover_thumbnail = Object.read(q.get('album_cover_thumbnail'))
        audio = Object.read(q.get('audio'))
        return Audio(duration, title, performer, file_name, mime_type, album_cover_minithumbnail, album_cover_thumbnail, audio)
