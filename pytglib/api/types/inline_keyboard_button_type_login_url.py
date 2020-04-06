

from ..utils import Object


class InlineKeyboardButtonTypeLoginUrl(Object):
    """
    A button that opens a specified URL and automatically logs in in current user if they allowed to do that 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeLoginUrl``

    Args:
        url (:obj:`str`):
            An HTTP URL to open 
        id (:obj:`int`):
            Unique button identifier 
        forward_text (:obj:`str`):
            If non-empty, new text of the button in forwarded messages

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeLoginUrl"

    def __init__(self, url, id, forward_text, **kwargs):
        
        self.url = url  # str
        self.id = id  # int
        self.forward_text = forward_text  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeLoginUrl":
        url = q.get('url')
        id = q.get('id')
        forward_text = q.get('forward_text')
        return InlineKeyboardButtonTypeLoginUrl(url, id, forward_text)
