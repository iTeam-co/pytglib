

from ..utils import Object


class CreateSecretChat(Object):
    """
    Returns an existing chat corresponding to a known secret chat 

    Attributes:
        ID (:obj:`str`): ``CreateSecretChat``

    Args:
        secret_chat_id (:obj:`int`):
            Secret chat identifier

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createSecretChat"

    def __init__(self, secret_chat_id, extra=None, **kwargs):
        self.extra = extra
        self.secret_chat_id = secret_chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CreateSecretChat":
        secret_chat_id = q.get('secret_chat_id')
        return CreateSecretChat(secret_chat_id)
