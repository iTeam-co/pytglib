

from ..utils import Object


class GetLoginUrlInfo(Object):
    """
    Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button

    Attributes:
        ID (:obj:`str`): ``GetLoginUrlInfo``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message with the button 
        message_id (:obj:`int`):
            Message identifier of the message with the button 
        button_id (:obj:`int`):
            Button identifier

    Returns:
        LoginUrlInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLoginUrlInfo"

    def __init__(self, chat_id, message_id, button_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.button_id = button_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetLoginUrlInfo":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        button_id = q.get('button_id')
        return GetLoginUrlInfo(chat_id, message_id, button_id)
