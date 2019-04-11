

from ..utils import Object


class InputInlineQueryResultAnimatedMpeg4(Object):
    """
    Represents a link to an animated (i.e. without sound) H.264/MPEG-4 AVC video 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultAnimatedMpeg4``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the result 
        thumbnail_url (:obj:`str`):
            URL of the static result thumbnail (JPEG or GIF), if it exists
        mpeg4_url (:obj:`str`):
            The URL of the MPEG4-file (file size must not exceed 1MB) 
        mpeg4_duration (:obj:`int`):
            Duration of the video, in seconds 
        mpeg4_width (:obj:`int`):
            Width of the video 
        mpeg4_height (:obj:`int`):
            Height of the video
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageAnimation, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultAnimatedMpeg4"

    def __init__(self, id, title, thumbnail_url, mpeg4_url, mpeg4_duration, mpeg4_width, mpeg4_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.thumbnail_url = thumbnail_url  # str
        self.mpeg4_url = mpeg4_url  # str
        self.mpeg4_duration = mpeg4_duration  # int
        self.mpeg4_width = mpeg4_width  # int
        self.mpeg4_height = mpeg4_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultAnimatedMpeg4":
        id = q.get('id')
        title = q.get('title')
        thumbnail_url = q.get('thumbnail_url')
        mpeg4_url = q.get('mpeg4_url')
        mpeg4_duration = q.get('mpeg4_duration')
        mpeg4_width = q.get('mpeg4_width')
        mpeg4_height = q.get('mpeg4_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultAnimatedMpeg4(id, title, thumbnail_url, mpeg4_url, mpeg4_duration, mpeg4_width, mpeg4_height, reply_markup, input_message_content)
