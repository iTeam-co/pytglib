

from ..utils import Object


class UpdateNewInlineCallbackQuery(Object):
    """
    A new incoming callback query from a message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewInlineCallbackQuery``

    Args:
        id (:obj:`int`):
            Unique query identifier 
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query 
        inline_message_id (:obj:`str`):
            Identifier of the inline message, from which the query originated
        chat_instance (:obj:`int`):
            An identifier uniquely corresponding to the chat a message was sent to 
        payload (:class:`telegram.api.types.CallbackQueryPayload`):
            Query payload

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewInlineCallbackQuery"

    def __init__(self, id, sender_user_id, inline_message_id, chat_instance, payload, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.inline_message_id = inline_message_id  # str
        self.chat_instance = chat_instance  # int
        self.payload = payload  # CallbackQueryPayload

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewInlineCallbackQuery":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        inline_message_id = q.get('inline_message_id')
        chat_instance = q.get('chat_instance')
        payload = Object.read(q.get('payload'))
        return UpdateNewInlineCallbackQuery(id, sender_user_id, inline_message_id, chat_instance, payload)
