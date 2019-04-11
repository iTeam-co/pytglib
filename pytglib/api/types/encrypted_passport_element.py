

from ..utils import Object


class EncryptedPassportElement(Object):
    """
    Contains information about an encrypted Telegram Passport element; for bots only 

    Attributes:
        ID (:obj:`str`): ``EncryptedPassportElement``

    Args:
        type (:class:`telegram.api.types.PassportElementType`):
            Type of Telegram Passport element 
        data (:obj:`bytes`):
            Encrypted JSON-encoded data about the user 
        front_side (:class:`telegram.api.types.datedFile`):
            The front side of an identity document 
        reverse_side (:class:`telegram.api.types.datedFile`):
            The reverse side of an identity document; may be null 
        selfie (:class:`telegram.api.types.datedFile`):
            Selfie with the document; may be null 
        translation (List of :class:`telegram.api.types.datedFile`):
            List of files containing a certified English translation of the document 
        files (List of :class:`telegram.api.types.datedFile`):
            List of attached files 
        value (:obj:`str`):
            Unencrypted data, phone number or email address 
        hash (:obj:`str`):
            Hash of the entire element

    Returns:
        EncryptedPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "encryptedPassportElement"

    def __init__(self, type, data, front_side, reverse_side, selfie, translation, files, value, hash, **kwargs):
        
        self.type = type  # PassportElementType
        self.data = data  # bytes
        self.front_side = front_side  # DatedFile
        self.reverse_side = reverse_side  # DatedFile
        self.selfie = selfie  # DatedFile
        self.translation = translation  # list of datedFile
        self.files = files  # list of datedFile
        self.value = value  # str
        self.hash = hash  # str

    @staticmethod
    def read(q: dict, *args) -> "EncryptedPassportElement":
        type = Object.read(q.get('type'))
        data = q.get('data')
        front_side = Object.read(q.get('front_side'))
        reverse_side = Object.read(q.get('reverse_side'))
        selfie = Object.read(q.get('selfie'))
        translation = [Object.read(i) for i in q.get('translation', [])]
        files = [Object.read(i) for i in q.get('files', [])]
        value = q.get('value')
        hash = q.get('hash')
        return EncryptedPassportElement(type, data, front_side, reverse_side, selfie, translation, files, value, hash)
