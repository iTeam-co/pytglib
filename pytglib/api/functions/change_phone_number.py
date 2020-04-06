

from ..utils import Object


class ChangePhoneNumber(Object):
    """
    Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code

    Attributes:
        ID (:obj:`str`): ``ChangePhoneNumber``

    Args:
        phone_number (:obj:`str`):
            The new phone number of the user in international format 
        settings (:class:`telegram.api.types.phoneNumberAuthenticationSettings`):
            Settings for the authentication of the user's phone number

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "changePhoneNumber"

    def __init__(self, phone_number, settings, extra=None, **kwargs):
        self.extra = extra
        self.phone_number = phone_number  # str
        self.settings = settings  # PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict, *args) -> "ChangePhoneNumber":
        phone_number = q.get('phone_number')
        settings = Object.read(q.get('settings'))
        return ChangePhoneNumber(phone_number, settings)
