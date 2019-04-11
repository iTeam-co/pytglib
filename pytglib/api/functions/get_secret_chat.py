

from ..utils import Object


class GetSecretChat(Object):
    """
    Returns information about a secret chat by its identifier. This is an offline request 

    Attributes:
        ID (:obj:`str`): ``GetSecretChat``

    Args:
        secret_chat_id (:obj:`int`):
            Secret chat identifier

    Returns:
        SecretChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSecretChat"

    def __init__(self, secret_chat_id, extra=None, **kwargs):
        self.extra = extra
        self.secret_chat_id = secret_chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetSecretChat":
        secret_chat_id = q.get('secret_chat_id')
        return GetSecretChat(secret_chat_id)
