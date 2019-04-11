

from ..utils import Object


class AuthorizationStateWaitEncryptionKey(Object):
    """
    TDLib needs an encryption key to decrypt the local database 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitEncryptionKey``

    Args:
        is_encrypted (:obj:`bool`):
            True, if the database is currently encrypted

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitEncryptionKey"

    def __init__(self, is_encrypted, **kwargs):
        
        self.is_encrypted = is_encrypted  # bool

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitEncryptionKey":
        is_encrypted = q.get('is_encrypted')
        return AuthorizationStateWaitEncryptionKey(is_encrypted)
