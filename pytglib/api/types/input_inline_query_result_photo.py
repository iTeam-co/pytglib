

from ..utils import Object


class InputInlineQueryResultPhoto(Object):
    """
    Represents link to a JPEG image 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultPhoto``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the result, if known 
        description (:obj:`str`):
            A short description of the result, if known 
        thumbnail_url (:obj:`str`):
            URL of the photo thumbnail, if it exists
        photo_url (:obj:`str`):
            The URL of the JPEG photo (photo size must not exceed 5MB) 
        photo_width (:obj:`int`):
            Width of the photo 
        photo_height (:obj:`int`):
            Height of the photo
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessagePhoto, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultPhoto"

    def __init__(self, id, title, description, thumbnail_url, photo_url, photo_width, photo_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.description = description  # str
        self.thumbnail_url = thumbnail_url  # str
        self.photo_url = photo_url  # str
        self.photo_width = photo_width  # int
        self.photo_height = photo_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultPhoto":
        id = q.get('id')
        title = q.get('title')
        description = q.get('description')
        thumbnail_url = q.get('thumbnail_url')
        photo_url = q.get('photo_url')
        photo_width = q.get('photo_width')
        photo_height = q.get('photo_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultPhoto(id, title, description, thumbnail_url, photo_url, photo_width, photo_height, reply_markup, input_message_content)
