

from ..utils import Object


class InputMessageAnimation(Object):
    """
    An animation message (GIF-style). 

    Attributes:
        ID (:obj:`str`): ``InputMessageAnimation``

    Args:
        animation (:class:`telegram.api.types.InputFile`):
            Animation file to be sent 
        thumbnail (:class:`telegram.api.types.inputThumbnail`):
            Animation thumbnail; pass null to skip thumbnail uploading 
        added_sticker_file_ids (List of :obj:`int`):
            File identifiers of the stickers added to the animation, if applicable
        duration (:obj:`int`):
            Duration of the animation, in seconds 
        width (:obj:`int`):
            Width of the animation; may be replaced by the server 
        height (:obj:`int`):
            Height of the animation; may be replaced by the server 
        caption (:class:`telegram.api.types.formattedText`):
            Animation caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageAnimation"

    def __init__(self, animation, thumbnail, added_sticker_file_ids, duration, width, height, caption, **kwargs):
        
        self.animation = animation  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.added_sticker_file_ids = added_sticker_file_ids  # list of int
        self.duration = duration  # int
        self.width = width  # int
        self.height = height  # int
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageAnimation":
        animation = Object.read(q.get('animation'))
        thumbnail = Object.read(q.get('thumbnail'))
        added_sticker_file_ids = q.get('added_sticker_file_ids')
        duration = q.get('duration')
        width = q.get('width')
        height = q.get('height')
        caption = Object.read(q.get('caption'))
        return InputMessageAnimation(animation, thumbnail, added_sticker_file_ids, duration, width, height, caption)
