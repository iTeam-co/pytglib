

from ..utils import Object


class MessageText(Object):
    """
    A text message 

    Attributes:
        ID (:obj:`str`): ``MessageText``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Text of the message 
        web_page (:class:`telegram.api.types.webPage`):
            A preview of the web page that's mentioned in the text; may be null

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageText"

    def __init__(self, text, web_page, **kwargs):
        
        self.text = text  # FormattedText
        self.web_page = web_page  # WebPage

    @staticmethod
    def read(q: dict, *args) -> "MessageText":
        text = Object.read(q.get('text'))
        web_page = Object.read(q.get('web_page'))
        return MessageText(text, web_page)
