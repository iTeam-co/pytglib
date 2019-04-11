

from ..utils import Object


class SetPassportElement(Object):
    """
    Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first 

    Attributes:
        ID (:obj:`str`): ``SetPassportElement``

    Args:
        element (:class:`telegram.api.types.InputPassportElement`):
            Input Telegram Passport element 
        password (:obj:`str`):
            Password of the current user

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPassportElement"

    def __init__(self, element, password, extra=None, **kwargs):
        self.extra = extra
        self.element = element  # InputPassportElement
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "SetPassportElement":
        element = Object.read(q.get('element'))
        password = q.get('password')
        return SetPassportElement(element, password)
