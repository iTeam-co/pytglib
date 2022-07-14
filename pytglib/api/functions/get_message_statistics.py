

from ..utils import Object


class GetMessageStatistics(Object):
    """
    Returns detailed statistics about a message. Can be used only if message.can_get_statistics == true 

    Attributes:
        ID (:obj:`str`): ``GetMessageStatistics``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        is_dark (:obj:`bool`):
            Pass true if a dark theme is used by the application

    Returns:
        MessageStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageStatistics"

    def __init__(self, chat_id, message_id, is_dark, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.is_dark = is_dark  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetMessageStatistics":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        is_dark = q.get('is_dark')
        return GetMessageStatistics(chat_id, message_id, is_dark)
