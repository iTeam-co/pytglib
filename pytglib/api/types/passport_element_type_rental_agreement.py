

from ..utils import Object


class PassportElementTypeRentalAgreement(Object):
    """
    A Telegram Passport element containing the user's rental agreement

    Attributes:
        ID (:obj:`str`): ``PassportElementTypeRentalAgreement``

    No parameters required.

    Returns:
        PassportElementType

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTypeRentalAgreement"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeRentalAgreement":
        
        return PassportElementTypeRentalAgreement()
