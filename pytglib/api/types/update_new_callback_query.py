

from ..utils import Object


class UpdateNewCallbackQuery(Object):
    """
    A new incoming callback query; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewCallbackQuery``

    Args:
        id (:obj:`int`):
            Unique query identifier 
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query
        chat_id (:obj:`int`):
            Identifier of the chat where the query was sent 
        message_id (:obj:`int`):
            Identifier of the message, from which the query originated
        chat_instance (:obj:`int`):
            Identifier that uniquely corresponds to the chat to which the message was sent 
        payload (:class:`telegram.api.types.CallbackQueryPayload`):
            Query payload

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewCallbackQuery"

    def __init__(self, id, sender_user_id, chat_id, message_id, chat_instance, payload, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.chat_instance = chat_instance  # int
        self.payload = payload  # CallbackQueryPayload

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewCallbackQuery":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        chat_instance = q.get('chat_instance')
        payload = Object.read(q.get('payload'))
        return UpdateNewCallbackQuery(id, sender_user_id, chat_id, message_id, chat_instance, payload)
