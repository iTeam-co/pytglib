

from ..utils import Object


class GetRepliedMessage(Object):
    """
    Returns information about a message that is replied by a given message. Also returns the pinned message, the game message, and the invoice message for messages of the types messagePinMessage, messageGameScore, and messagePaymentSuccessful respectively

    Attributes:
        ID (:obj:`str`): ``GetRepliedMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the reply message

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRepliedMessage"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetRepliedMessage":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetRepliedMessage(chat_id, message_id)
