

from ..utils import Object


class InputInlineQueryResultContact(Object):
    """
    Represents a user contact 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultContact``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        contact (:class:`telegram.api.types.contact`):
            User contact 
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
    ID = "inputInlineQueryResultContact"

    def __init__(self, id, contact, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.contact = contact  # Contact
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_width = thumbnail_width  # int
        self.thumbnail_height = thumbnail_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultContact":
        id = q.get('id')
        contact = Object.read(q.get('contact'))
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_width = q.get('thumbnail_width')
        thumbnail_height = q.get('thumbnail_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultContact(id, contact, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content)
