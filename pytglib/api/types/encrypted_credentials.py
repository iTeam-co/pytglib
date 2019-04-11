

from ..utils import Object


class EncryptedCredentials(Object):
    """
    Contains encrypted Telegram Passport data credentials 

    Attributes:
        ID (:obj:`str`): ``EncryptedCredentials``

    Args:
        data (:obj:`bytes`):
            The encrypted credentials 
        hash (:obj:`bytes`):
            The decrypted data hash 
        secret (:obj:`bytes`):
            Secret for data decryption, encrypted with the service's public key

    Returns:
        EncryptedCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "encryptedCredentials"

    def __init__(self, data, hash, secret, **kwargs):
        
        self.data = data  # bytes
        self.hash = hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(q: dict, *args) -> "EncryptedCredentials":
        data = q.get('data')
        hash = q.get('hash')
        secret = q.get('secret')
        return EncryptedCredentials(data, hash, secret)
