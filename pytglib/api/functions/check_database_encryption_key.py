

from ..utils import Object


class CheckDatabaseEncryptionKey(Object):
    """
    Checks the database encryption key for correctness. Works only when the current authorization state is authorizationStateWaitEncryptionKey 

    Attributes:
        ID (:obj:`str`): ``CheckDatabaseEncryptionKey``

    Args:
        encryption_key (:obj:`bytes`):
            Encryption key to check or set up

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkDatabaseEncryptionKey"

    def __init__(self, encryption_key, extra=None, **kwargs):
        self.extra = extra
        self.encryption_key = encryption_key  # bytes

    @staticmethod
    def read(q: dict, *args) -> "CheckDatabaseEncryptionKey":
        encryption_key = q.get('encryption_key')
        return CheckDatabaseEncryptionKey(encryption_key)
