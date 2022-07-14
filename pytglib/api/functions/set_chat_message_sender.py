

from ..utils import Object


class SetChatMessageSender(Object):
    """
    Selects a message sender to send messages in a chat 

    Attributes:
        ID (:obj:`str`): ``SetChatMessageSender``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_sender_id (:class:`telegram.api.types.MessageSender`):
            New message sender for the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatMessageSender"

    def __init__(self, chat_id, message_sender_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_sender_id = message_sender_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "SetChatMessageSender":
        chat_id = q.get('chat_id')
        message_sender_id = Object.read(q.get('message_sender_id'))
        return SetChatMessageSender(chat_id, message_sender_id)
