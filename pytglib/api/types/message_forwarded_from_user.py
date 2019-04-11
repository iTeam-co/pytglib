

from ..utils import Object


class MessageForwardedFromUser(Object):
    """
    The message was originally written by a known user 

    Attributes:
        ID (:obj:`str`): ``MessageForwardedFromUser``

    Args:
        sender_user_id (:obj:`int`):
            Identifier of the user that originally sent this message 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the message was originally sent
        forwarded_from_chat_id (:obj:`int`):
            For messages forwarded to the chat with the current user (saved messages), the identifier of the chat from which the message was forwarded; 0 if unknown
        forwarded_from_message_id (:obj:`int`):
            For messages forwarded to the chat with the current user (saved messages) the identifier of the original message from which the new message was forwarded; 0 if unknown

    Returns:
        MessageForwardInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardedFromUser"

    def __init__(self, sender_user_id, date, forwarded_from_chat_id, forwarded_from_message_id, **kwargs):
        
        self.sender_user_id = sender_user_id  # int
        self.date = date  # int
        self.forwarded_from_chat_id = forwarded_from_chat_id  # int
        self.forwarded_from_message_id = forwarded_from_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardedFromUser":
        sender_user_id = q.get('sender_user_id')
        date = q.get('date')
        forwarded_from_chat_id = q.get('forwarded_from_chat_id')
        forwarded_from_message_id = q.get('forwarded_from_message_id')
        return MessageForwardedFromUser(sender_user_id, date, forwarded_from_chat_id, forwarded_from_message_id)
