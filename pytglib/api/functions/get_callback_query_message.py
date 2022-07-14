

from ..utils import Object


class GetCallbackQueryMessage(Object):
    """
    Returns information about a message with the callback button that originated a callback query; for bots only 

    Attributes:
        ID (:obj:`str`): ``GetCallbackQueryMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat the message belongs to 
        message_id (:obj:`int`):
            Message identifier 
        callback_query_id (:obj:`int`):
            Identifier of the callback query

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCallbackQueryMessage"

    def __init__(self, chat_id, message_id, callback_query_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.callback_query_id = callback_query_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetCallbackQueryMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        callback_query_id = q.get('callback_query_id')
        return GetCallbackQueryMessage(chat_id, message_id, callback_query_id)
