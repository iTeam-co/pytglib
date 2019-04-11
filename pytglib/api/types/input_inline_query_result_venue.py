

from ..utils import Object


class InputInlineQueryResultVenue(Object):
    """
    Represents information about a venue 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultVenue``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        venue (:class:`telegram.api.types.venue`):
            Venue result 
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
    ID = "inputInlineQueryResultVenue"

    def __init__(self, id, venue, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.venue = venue  # Venue
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_width = thumbnail_width  # int
        self.thumbnail_height = thumbnail_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultVenue":
        id = q.get('id')
        venue = Object.read(q.get('venue'))
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_width = q.get('thumbnail_width')
        thumbnail_height = q.get('thumbnail_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultVenue(id, venue, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content)
