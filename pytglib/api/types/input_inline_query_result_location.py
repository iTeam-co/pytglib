

from ..utils import Object


class InputInlineQueryResultLocation(Object):
    """
    Represents a point on the map 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultLocation``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        location (:class:`telegram.api.types.location`):
            Location result 
        live_period (:obj:`int`):
            Amount of time relative to the message sent time until the location can be updated, in seconds 
        title (:obj:`str`):
            Title of the result 
        thumbnail_url (:obj:`str`):
            URL of the result thumbnail, if it exists 
        thumbnail_width (:obj:`int`):
            Thumbnail width, if known 
        thumbnail_height (:obj:`int`):
            Thumbnail height, if known
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultLocation"

    def __init__(self, id, location, live_period, title, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.location = location  # Location
        self.live_period = live_period  # int
        self.title = title  # str
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_width = thumbnail_width  # int
        self.thumbnail_height = thumbnail_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultLocation":
        id = q.get('id')
        location = Object.read(q.get('location'))
        live_period = q.get('live_period')
        title = q.get('title')
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_width = q.get('thumbnail_width')
        thumbnail_height = q.get('thumbnail_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultLocation(id, location, live_period, title, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content)
