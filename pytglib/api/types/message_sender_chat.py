

from ..utils import Object


class MessageSenderChat(Object):
    """
    The message was sent on behalf of a chat 

    Attributes:
        ID (:obj:`str`): ``MessageSenderChat``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat that sent the message

    Returns:
        MessageSender

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSenderChat"

    def __init__(self, chat_id, **kwargs):
        
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageSenderChat":
        chat_id = q.get('chat_id')
        return MessageSenderChat(chat_id)
