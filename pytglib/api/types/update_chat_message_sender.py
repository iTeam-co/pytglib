

from ..utils import Object


class UpdateChatMessageSender(Object):
    """
    The message sender that is selected to send messages in a chat has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatMessageSender``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_sender_id (:class:`telegram.api.types.MessageSender`):
            New value of message_sender_id; may be null if the user can't change message sender

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatMessageSender"

    def __init__(self, chat_id, message_sender_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_sender_id = message_sender_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatMessageSender":
        chat_id = q.get('chat_id')
        message_sender_id = Object.read(q.get('message_sender_id'))
        return UpdateChatMessageSender(chat_id, message_sender_id)
