

from ..utils import Object


class MessageForwardOriginChannel(Object):
    """
    The message was originally a post in a channel

    Attributes:
        ID (:obj:`str`): ``MessageForwardOriginChannel``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat from which the message was originally forwarded
        message_id (:obj:`int`):
            Message identifier of the original message; 0 if unknown
        author_signature (:obj:`str`):
            Original post author signature

    Returns:
        MessageForwardOrigin

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardOriginChannel"

    def __init__(self, chat_id, message_id, author_signature, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.author_signature = author_signature  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginChannel":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        author_signature = q.get('author_signature')
        return MessageForwardOriginChannel(chat_id, message_id, author_signature)
