

from ..utils import Object


class InputMessageAudio(Object):
    """
    An audio message 

    Attributes:
        ID (:obj:`str`): ``InputMessageAudio``

    Args:
        audio (:class:`telegram.api.types.InputFile`):
            Audio file to be sent 
        album_cover_thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Thumbnail of the cover for the album, if available 
        duration (:obj:`int`):
            Duration of the audio, in seconds; may be replaced by the server 
        title (:obj:`str`):
            Title of the audio; 0-64 characters; may be replaced by the server
        performer (:obj:`str`):
            Performer of the audio; 0-64 characters, may be replaced by the server 
        caption (:class:`telegram.api.types.formattedText`):
            Audio caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageAudio"

    def __init__(self, audio, album_cover_thumbnail, duration, title, performer, caption, **kwargs):
        
        self.audio = audio  # InputFile
        self.album_cover_thumbnail = album_cover_thumbnail  # InputThumbnail
        self.duration = duration  # int
        self.title = title  # str
        self.performer = performer  # str
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageAudio":
        audio = Object.read(q.get('audio'))
        album_cover_thumbnail = Object.read(q.get('album_cover_thumbnail'))
        duration = q.get('duration')
        title = q.get('title')
        performer = q.get('performer')
        caption = Object.read(q.get('caption'))
        return InputMessageAudio(audio, album_cover_thumbnail, duration, title, performer, caption)
