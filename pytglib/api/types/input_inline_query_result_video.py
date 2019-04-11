

from ..utils import Object


class InputInlineQueryResultVideo(Object):
    """
    Represents a link to a page containing an embedded video player or a video file 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultVideo``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the result 
        description (:obj:`str`):
            A short description of the result, if known
        thumbnail_url (:obj:`str`):
            The URL of the video thumbnail (JPEG), if it exists 
        video_url (:obj:`str`):
            URL of the embedded video player or video file 
        mime_type (:obj:`str`):
            MIME type of the content of the video URL, only "text/html" or "video/mp4" are currently supported
        video_width (:obj:`int`):
            Width of the video 
        video_height (:obj:`int`):
            Height of the video 
        video_duration (:obj:`int`):
            Video duration, in seconds
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageVideo, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultVideo"

    def __init__(self, id, title, description, thumbnail_url, video_url, mime_type, video_width, video_height, video_duration, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.description = description  # str
        self.thumbnail_url = thumbnail_url  # str
        self.video_url = video_url  # str
        self.mime_type = mime_type  # str
        self.video_width = video_width  # int
        self.video_height = video_height  # int
        self.video_duration = video_duration  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultVideo":
        id = q.get('id')
        title = q.get('title')
        description = q.get('description')
        thumbnail_url = q.get('thumbnail_url')
        video_url = q.get('video_url')
        mime_type = q.get('mime_type')
        video_width = q.get('video_width')
        video_height = q.get('video_height')
        video_duration = q.get('video_duration')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultVideo(id, title, description, thumbnail_url, video_url, mime_type, video_width, video_height, video_duration, reply_markup, input_message_content)
