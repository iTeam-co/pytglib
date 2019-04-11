

from ..utils import Object


class InputInlineQueryResultArticle(Object):
    """
    Represents a link to an article or web page 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultArticle``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        url (:obj:`str`):
            URL of the result, if it exists 
        hide_url (:obj:`bool`):
            True, if the URL must be not shown 
        title (:obj:`str`):
            Title of the result
        description (:obj:`str`):
            A short description of the result 
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
    ID = "inputInlineQueryResultArticle"

    def __init__(self, id, url, hide_url, title, description, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.url = url  # str
        self.hide_url = hide_url  # bool
        self.title = title  # str
        self.description = description  # str
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_width = thumbnail_width  # int
        self.thumbnail_height = thumbnail_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultArticle":
        id = q.get('id')
        url = q.get('url')
        hide_url = q.get('hide_url')
        title = q.get('title')
        description = q.get('description')
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_width = q.get('thumbnail_width')
        thumbnail_height = q.get('thumbnail_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultArticle(id, url, hide_url, title, description, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content)
