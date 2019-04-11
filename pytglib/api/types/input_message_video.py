

from ..utils import Object


class InputMessageVideo(Object):
    """
    A video message 

    Attributes:
        ID (:obj:`str`): ``InputMessageVideo``

    Args:
        video (:class:`telegram.api.types.InputFile`):
            Video to be sent 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Video thumbnail, if available 
        added_sticker_file_ids (List of :obj:`int`):
            File identifiers of the stickers added to the video, if applicable
        duration (:obj:`int`):
            Duration of the video, in seconds 
        width (:obj:`int`):
            Video width 
        height (:obj:`int`):
            Video height 
        supports_streaming (:obj:`bool`):
            True, if the video should be tried to be streamed
        caption (:class:`telegram.api.types.formattedText`):
            Video caption; 0-GetOption("message_caption_length_max") characters 
        ttl (:obj:`int`):
            Video TTL (Time To Live), in seconds (0-60)A non-zero TTL can be specified only in private chats

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageVideo"

    def __init__(self, video, thumbnail, added_sticker_file_ids, duration, width, height, supports_streaming, caption, ttl, **kwargs):
        
        self.video = video  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.added_sticker_file_ids = added_sticker_file_ids  # list of int
        self.duration = duration  # int
        self.width = width  # int
        self.height = height  # int
        self.supports_streaming = supports_streaming  # bool
        self.caption = caption  # FormattedText
        self.ttl = ttl  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessageVideo":
        video = Object.read(q.get('video'))
        thumbnail = Object.read(q.get('thumbnail'))
        added_sticker_file_ids = q.get('added_sticker_file_ids')
        duration = q.get('duration')
        width = q.get('width')
        height = q.get('height')
        supports_streaming = q.get('supports_streaming')
        caption = Object.read(q.get('caption'))
        ttl = q.get('ttl')
        return InputMessageVideo(video, thumbnail, added_sticker_file_ids, duration, width, height, supports_streaming, caption, ttl)
