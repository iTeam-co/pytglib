

from ..utils import Object


class PassportElementRentalAgreement(Object):
    """
    A Telegram Passport element containing the user's rental agreement 

    Attributes:
        ID (:obj:`str`): ``PassportElementRentalAgreement``

    Args:
        rental_agreement (:class:`telegram.api.types.personalDocument`):
            Rental agreement

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementRentalAgreement"

    def __init__(self, rental_agreement, **kwargs):
        
        self.rental_agreement = rental_agreement  # PersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementRentalAgreement":
        rental_agreement = Object.read(q.get('rental_agreement'))
        return PassportElementRentalAgreement(rental_agreement)
