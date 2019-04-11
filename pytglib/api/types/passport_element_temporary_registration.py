

from ..utils import Object


class PassportElementTemporaryRegistration(Object):
    """
    A Telegram Passport element containing the user's temporary registration 

    Attributes:
        ID (:obj:`str`): ``PassportElementTemporaryRegistration``

    Args:
        temporary_registration (:class:`telegram.api.types.personalDocument`):
            Temporary registration

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementTemporaryRegistration"

    def __init__(self, temporary_registration, **kwargs):
        
        self.temporary_registration = temporary_registration  # PersonalDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTemporaryRegistration":
        temporary_registration = Object.read(q.get('temporary_registration'))
        return PassportElementTemporaryRegistration(temporary_registration)
