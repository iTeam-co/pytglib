

from ..utils import Object


class InputInlineQueryResultSticker(Object):
    """
    Represents a link to a WEBP or TGS sticker 

    Attributes:
        ID (:obj:`str`): ``InputInlineQueryResultSticker``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        thumbnail_url (:obj:`str`):
            URL of the sticker thumbnail, if it exists
        sticker_url (:obj:`str`):
            The URL of the WEBP or TGS sticker (sticker file size must not exceed 5MB) 
        sticker_width (:obj:`int`):
            Width of the sticker 
        sticker_height (:obj:`int`):
            Height of the sticker
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The message reply markupMust be of type replyMarkupInlineKeyboard or null
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sentMust be one of the following types: InputMessageText, inputMessageSticker, InputMessageLocation, InputMessageVenue or InputMessageContact

    Returns:
        InputInlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInlineQueryResultSticker"

    def __init__(self, id, thumbnail_url, sticker_url, sticker_width, sticker_height, reply_markup, input_message_content, **kwargs):
        
        self.id = id  # str
        self.thumbnail_url = thumbnail_url  # str
        self.sticker_url = sticker_url  # str
        self.sticker_width = sticker_width  # int
        self.sticker_height = sticker_height  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "InputInlineQueryResultSticker":
        id = q.get('id')
        thumbnail_url = q.get('thumbnail_url')
        sticker_url = q.get('sticker_url')
        sticker_width = q.get('sticker_width')
        sticker_height = q.get('sticker_height')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return InputInlineQueryResultSticker(id, thumbnail_url, sticker_url, sticker_width, sticker_height, reply_markup, input_message_content)
