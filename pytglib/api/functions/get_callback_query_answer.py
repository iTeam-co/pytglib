

from ..utils import Object


class GetCallbackQueryAnswer(Object):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires 

    Attributes:
        ID (:obj:`str`): ``GetCallbackQueryAnswer``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat with the message 
        message_id (:obj:`int`):
            Identifier of the message from which the query originated 
        payload (:class:`telegram.api.types.CallbackQueryPayload`):
            Query payload

    Returns:
        CallbackQueryAnswer

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCallbackQueryAnswer"

    def __init__(self, chat_id, message_id, payload, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.payload = payload  # CallbackQueryPayload

    @staticmethod
    def read(q: dict, *args) -> "GetCallbackQueryAnswer":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        payload = Object.read(q.get('payload'))
        return GetCallbackQueryAnswer(chat_id, message_id, payload)
