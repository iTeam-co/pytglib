

from ..utils import Object


class MessageForwardedPost(Object):
    """
    The message was originally a post in a channel 

    Attributes:
        ID (:obj:`str`): ``MessageForwardedPost``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat from which the message was forwarded 
        author_signature (:obj:`str`):
            Post author signature
        date (:obj:`int`):
            Point in time (Unix timestamp) when the message was originally sent 
        message_id (:obj:`int`):
            Message identifier of the original message from which the new message was forwarded; 0 if unknown
        forwarded_from_chat_id (:obj:`int`):
            For messages forwarded to the chat with the current user (saved messages), the identifier of the chat from which the message was forwarded; 0 if unknown
        forwarded_from_message_id (:obj:`int`):
            For messages forwarded to the chat with the current user (saved messages), the identifier of the original message from which the new message was forwarded; 0 if unknown

    Returns:
        MessageForwardInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardedPost"

    def __init__(self, chat_id, author_signature, date, message_id, forwarded_from_chat_id, forwarded_from_message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.author_signature = author_signature  # str
        self.date = date  # int
        self.message_id = message_id  # int
        self.forwarded_from_chat_id = forwarded_from_chat_id  # int
        self.forwarded_from_message_id = forwarded_from_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardedPost":
        chat_id = q.get('chat_id')
        author_signature = q.get('author_signature')
        date = q.get('date')
        message_id = q.get('message_id')
        forwarded_from_chat_id = q.get('forwarded_from_chat_id')
        forwarded_from_message_id = q.get('forwarded_from_message_id')
        return MessageForwardedPost(chat_id, author_signature, date, message_id, forwarded_from_chat_id, forwarded_from_message_id)
