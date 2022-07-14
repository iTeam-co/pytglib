

from ..utils import Object


class MessageSenderUser(Object):
    """
    The message was sent by a known user 

    Attributes:
        ID (:obj:`str`): ``MessageSenderUser``

    Args:
        user_id (:obj:`int`):
            Identifier of the user that sent the message

    Returns:
        MessageSender

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSenderUser"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageSenderUser":
        user_id = q.get('user_id')
        return MessageSenderUser(user_id)
