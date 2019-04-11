

from ..utils import Object


class InputInlineQueryResultAnimatedGif(Object):
    """
    Represents a link to an animated GIF 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultAnimatedGif``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the query result 
        thumbnail_url (:obj:`str`):
            URL of the static result thumbnail (JPEG or GIF), if it exists
        gif_url (:obj:`str`):
            The URL of the GIF-file (file size must not exceed 1MB) 
        gif_duration (:obj:`int`):
            Duration of the GIF, in seconds 
        gif_width (:obj:`int`):
            Width of the GIF 
        gif_height (:obj:`int`):
            Height of the GIF
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageAnimation, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultAnimatedGif"

    def __init__(self, id, title, thumbnail_url, gif_url, gif_duration, gif_width, gif_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.thumbnail_url = thumbnail_url  # str
        self.gif_url = gif_url  # str
        self.gif_duration = gif_duration  # int
        self.gif_width = gif_width  # int
        self.gif_height = gif_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultAnimatedGif":
        id = q.get('id')
        title = q.get('title')
        thumbnail_url = q.get('thumbnail_url')
        gif_url = q.get('gif_url')
        gif_duration = q.get('gif_duration')
        gif_width = q.get('gif_width')
        gif_height = q.get('gif_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultAnimatedGif(id, title, thumbnail_url, gif_url, gif_duration, gif_width, gif_height, reply_markup, input_message_content)
