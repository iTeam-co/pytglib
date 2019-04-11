

from ..utils import Object


class SetDatabaseEncryptionKey(Object):
    """
    Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain 

    Attributes:
        ID (:obj:`str`): ``SetDatabaseEncryptionKey``

    Args:
        new_encryption_key (:obj:`bytes`):
            New encryption key

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setDatabaseEncryptionKey"

    def __init__(self, new_encryption_key, extra=None, **kwargs):
        self.extra = extra
        self.new_encryption_key = new_encryption_key  # bytes

    @staticmethod
    def read(q: dict, *args) -> "SetDatabaseEncryptionKey":
        new_encryption_key = q.get('new_encryption_key')
        return SetDatabaseEncryptionKey(new_encryption_key)
