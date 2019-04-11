

from ..utils import Object


class UpdateSecretChat(Object):
    """
    Some data of a secret chat has changed. This update is guaranteed to come before the secret chat identifier is returned to the client 

    Attributes:
        ID (:obj:`str`): ``UpdateSecretChat``

    Args:
        secret_chat (:class:`telegram.api.types.secretChat`):
            New data about the secret chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSecretChat"

    def __init__(self, secret_chat, **kwargs):
        
        self.secret_chat = secret_chat  # SecretChat

    @staticmethod
    def read(q: dict, *args) -> "UpdateSecretChat":
        secret_chat = Object.read(q.get('secret_chat'))
        return UpdateSecretChat(secret_chat)
