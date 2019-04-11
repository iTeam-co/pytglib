

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
            Animation thumbnail, if available 
        duration (:obj:`int`):
            Duration of the animation, in seconds 
        width (:obj:`int`):
            Width of the animation; may be replaced by the server 
        height (:obj:`int`):
            Height of the animation; may be replaced by the server 
        caption (:class:`telegram.api.types.formattedText`):
            Animation caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageAnimation"

    def __init__(self, animation, thumbnail, duration, width, height, caption, **kwargs):
        
        self.animation = animation  # InputFile
        self.thumbnail = thumbnail  # InputThumbnail
        self.duration = duration  # int
        self.width = width  # int
        self.height = height  # int
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "InputMessageAnimation":
        animation = Object.read(q.get('animation'))
        thumbnail = Object.read(q.get('thumbnail'))
        duration = q.get('duration')
        width = q.get('width')
        height = q.get('height')
        caption = Object.read(q.get('caption'))
        return InputMessageAnimation(animation, thumbnail, duration, width, height, caption)
