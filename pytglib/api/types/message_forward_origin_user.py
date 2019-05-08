

from ..utils import Object


class MessageForwardOriginUser(Object):
    """
    The message was originally written by a known user 

    Attributes:
        ID (:obj:`str`): ``MessageForwardOriginUser``

    Args:
        sender_user_id (:obj:`int`):
            Identifier of the user that originally sent the message

    Returns:
        MessageForwardOrigin

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageForwardOriginUser"

    def __init__(self, sender_user_id, **kwargs):
        
        self.sender_user_id = sender_user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageForwardOriginUser":
        sender_user_id = q.get('sender_user_id')
        return MessageForwardOriginUser(sender_user_id)
