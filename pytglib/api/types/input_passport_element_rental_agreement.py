

from ..utils import Object


class InputPassportElementRentalAgreement(Object):
    """
    A Telegram Passport element to be saved containing the user's rental agreement 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementRentalAgreement``

    Args:
        rental_agreement (:class:`telegram.api.types.inputPersonalDocument`):
            The rental agreement to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementRentalAgreement"

    def __init__(self, rental_agreement, **kwargs):
        
        self.rental_agreement = rental_agreement  # InputPersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementRentalAgreement":
        rental_agreement = Object.read(q.get('rental_agreement'))
        return InputPassportElementRentalAgreement(rental_agreement)
