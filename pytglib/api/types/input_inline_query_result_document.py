

from ..utils import Object


class InputInlineQueryResultDocument(Object):
    """
    Represents a link to a file 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultDocument``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        title (:obj:`str`):
            Title of the resulting file 
        description (:obj:`str`):
            Short description of the result, if known 
        document_url (:obj:`str`):
            URL of the file 
        mime_type (:obj:`str`):
            MIME type of the file content; only "application/pdf" and "application/zip" are currently allowed
        thumbnail_url (:obj:`str`):
            The URL of the file thumbnail, if it exists 
        thumbnail_width (:obj:`int`):
            Width of the thumbnail 
        thumbnail_height (:obj:`int`):
            Height of the thumbnail
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, InputMessageDocument, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultDocument"

    def __init__(self, id, title, description, document_url, mime_type, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.description = description  # str
        self.document_url = document_url  # str
        self.mime_type = mime_type  # str
        self.thumbnail_url = thumbnail_url  # str
        self.thumbnail_width = thumbnail_width  # int
        self.thumbnail_height = thumbnail_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultDocument":
        id = q.get('id')
        title = q.get('title')
        description = q.get('description')
        document_url = q.get('document_url')
        mime_type = q.get('mime_type')
        thumbnail_url = q.get('thumbnail_url')
        thumbnail_width = q.get('thumbnail_width')
        thumbnail_height = q.get('thumbnail_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultDocument(id, title, description, document_url, mime_type, thumbnail_url, thumbnail_width, thumbnail_height, reply_markup, input_message_content)
