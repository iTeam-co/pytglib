

from ..utils import Object


class IdentityDocument(Object):
    """
    An identity document 

    Attributes:
        ID (:obj:`str`): ``IdentityDocument``

    Args:
        number (:obj:`str`):
            Document number; 1-24 characters 
        expiry_date (:class:`telegram.api.types.date`):
            Document expiry date; may be null 
        front_side (:class:`telegram.api.types.datedFile`):
            Front side of the document
        reverse_side (:class:`telegram.api.types.datedFile`):
            Reverse side of the document; only for driver license and identity card 
        selfie (:class:`telegram.api.types.datedFile`):
            Selfie with the document; may be null 
        translation (List of :class:`telegram.api.types.datedFile`):
            List of files containing a certified English translation of the document

    Returns:
        IdentityDocument

    Raises:
        :class:`telegram.Error`
    """
    ID = "identityDocument"

    def __init__(self, number, expiry_date, front_side, reverse_side, selfie, translation, **kwargs):
        
        self.number = number  # str
        self.expiry_date = expiry_date  # Date
        self.front_side = front_side  # DatedFile
        self.reverse_side = reverse_side  # DatedFile
        self.selfie = selfie  # DatedFile
        self.translation = translation  # list of datedFile

    @staticmethod
    def read(q: dict, *args) -> "IdentityDocument":
        number = q.get('number')
        expiry_date = Object.read(q.get('expiry_date'))
        front_side = Object.read(q.get('front_side'))
        reverse_side = Object.read(q.get('reverse_side'))
        selfie = Object.read(q.get('selfie'))
        translation = [Object.read(i) for i in q.get('translation', [])]
        return IdentityDocument(number, expiry_date, front_side, reverse_side, selfie, translation)
