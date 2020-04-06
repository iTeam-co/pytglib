

from ..utils import Object


class CloseSecretChat(Object):
    """
    Closes a secret chat, effectively transferring its state to secretChatStateClosed 

    Attributes:
        ID (:obj:`str`): ``CloseSecretChat``

    Args:
        secret_chat_id (:obj:`int`):
            Secret chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "closeSecretChat"

    def __init__(self, secret_chat_id, extra=None, **kwargs):
        self.extra = extra
        self.secret_chat_id = secret_chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CloseSecretChat":
        secret_chat_id = q.get('secret_chat_id')
        return CloseSecretChat(secret_chat_id)
