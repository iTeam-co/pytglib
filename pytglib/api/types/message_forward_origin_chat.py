

from ..utils import Object


class MessageForwardOriginChat(Object):
    """
    The message was originally sent on behalf of a chat

    Attributes:
        ID (:obj:`str`): ``MessageForwardOriginChat``

    Args:
        sender_chat_id (:obj:`int`):
            Identifier of the chat that originally sent the message
        author_signature (:obj:`str`):
            For messages originally sent by an anonymous chat administrator, original message author signature

    Returns:
        MessageForwardOrigin

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardOriginChat"

    def __init__(self, sender_chat_id, author_signature, **kwargs):
        
        self.sender_chat_id = sender_chat_id  # int
        self.author_signature = author_signature  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginChat":
        sender_chat_id = q.get('sender_chat_id')
        author_signature = q.get('author_signature')
        return MessageForwardOriginChat(sender_chat_id, author_signature)
