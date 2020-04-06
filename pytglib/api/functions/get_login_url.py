

from ..utils import Object


class GetLoginUrl(Object):
    """
    Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl.Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button

    Attributes:
        ID (:obj:`str`): ``GetLoginUrl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message with the button 
        message_id (:obj:`int`):
            Message identifier of the message with the button 
        button_id (:obj:`int`):
            Button identifier
        allow_write_access (:obj:`bool`):
            True, if the user allowed the bot to send them messages

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getLoginUrl"

    def __init__(self, chat_id, message_id, button_id, allow_write_access, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.button_id = button_id  # int
        self.allow_write_access = allow_write_access  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetLoginUrl":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        button_id = q.get('button_id')
        allow_write_access = q.get('allow_write_access')
        return GetLoginUrl(chat_id, message_id, button_id, allow_write_access)
