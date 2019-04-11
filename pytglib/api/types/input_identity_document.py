

from ..utils import Object


class InputIdentityDocument(Object):
    """
    An identity document to be saved to Telegram Passport 

    Attributes:
        ID (:obj:`str`): ``InputIdentityDocument``

    Args:
        number (:obj:`str`):
            Document number; 1-24 characters 
        expiry_date (:class:`telegram.api.types.date`):
            Document expiry date, if available 
        front_side (:class:`telegram.api.types.InputFile`):
            Front side of the document
        reverse_side (:class:`telegram.api.types.InputFile`):
            Reverse side of the document; only for driver license and identity card 
        selfie (:class:`telegram.api.types.InputFile`):
            Selfie with the document, if available 
        translation (List of :class:`telegram.api.types.InputFile`):
            List of files containing a certified English translation of the document

    Returns:
        InputIdentityDocument

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputIdentityDocument"

    def __init__(self, number, expiry_date, front_side, reverse_side, selfie, translation, **kwargs):
        
        self.number = number  # str
        self.expiry_date = expiry_date  # Date
        self.front_side = front_side  # InputFile
        self.reverse_side = reverse_side  # InputFile
        self.selfie = selfie  # InputFile
        self.translation = translation  # list of InputFile

    @staticmethod
    def read(q: dict, *args) -> "InputIdentityDocument":
        number = q.get('number')
        expiry_date = Object.read(q.get('expiry_date'))
        front_side = Object.read(q.get('front_side'))
        reverse_side = Object.read(q.get('reverse_side'))
        selfie = Object.read(q.get('selfie'))
        translation = [Object.read(i) for i in q.get('translation', [])]
        return InputIdentityDocument(number, expiry_date, front_side, reverse_side, selfie, translation)
