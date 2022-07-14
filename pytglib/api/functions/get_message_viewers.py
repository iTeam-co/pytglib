

from ..utils import Object


class GetMessageViewers(Object):
    """
    Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if message.can_get_viewers == true 

    Attributes:
        ID (:obj:`str`): ``GetMessageViewers``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Identifier of the message

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageViewers"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageViewers":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessageViewers(chat_id, message_id)
