

from ..utils import Object


class InputInlineQueryResultAnimation(Object):
    """
    Represents a link to an animated GIF or an animated (i.e., without sound) H.264/MPEG-4 AVC video

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultAnimation``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the query result
        thumbnail_url (:obj:`str`):
            URL of the result thumbnail (JPEG, GIF, or MPEG4), if it exists 
        thumbnail_mime_type (:obj:`str`):
            MIME type of the video thumbnailIf non-empty, must be one of "image/jpeg", "image/gif" and "video/mp4"
        video_url (:obj:`str`):
            The URL of the video file (file size must not exceed 1MB) 
        video_mime_type (:obj:`str`):
            MIME type of the video fileMust be one of "image/gif" and "video/mp4"
        video_duration (:obj:`int`):
            Duration of the video, in seconds 
        video_width (:obj:`int`):
            Width of the video 
        video_height (:obj:`int`):
            Height of the video
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markup; pass null if noneMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: inputMessageText, inputMessageAnimation, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultAnimation"

    def __init__(self, id, title, thumbnail_url, thumbnail_mime_type, video_url, video_mime_type, video_duration, video_width, video_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_mime_type = thumbnail_mime_type  # str
        self.video_url = video_url  # str
        self.video_mime_type = video_mime_type  # str
        self.video_duration = video_duration  # int
        self.video_width = video_width  # int
        self.video_height = video_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultAnimation":
        id = q.get('id')
        title = q.get('title')
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_mime_type = q.get('thumbnail_mime_type')
        video_url = q.get('video_url')
        video_mime_type = q.get('video_mime_type')
        video_duration = q.get('video_duration')
        video_width = q.get('video_width')
        video_height = q.get('video_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultAnimation(id, title, thumbnail_url, thumbnail_mime_type, video_url, video_mime_type, video_duration, video_width, video_height, reply_markup, input_message_content)
