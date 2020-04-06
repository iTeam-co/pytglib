

from ..utils import Object


class SendPhoneNumberVerificationCode(Object):
    """
    Sends a code to verify a phone number to be added to a user's Telegram Passport

    Attributes:
        ID (:obj:`str`): ``SendPhoneNumberVerificationCode``

    Args:
        phone_number (:obj:`str`):
            The phone number of the user, in international format 
        settings (:class:`telegram.api.types.phoneNumberAuthenticationSettings`):
            Settings for the authentication of the user's phone number

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPhoneNumberVerificationCode"

    def __init__(self, phone_number, settings, extra=None, **kwargs):
        self.extra = extra
        self.phone_number = phone_number  # str
        self.settings = settings  # PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict, *args) -> "SendPhoneNumberVerificationCode":
        phone_number = q.get('phone_number')
        settings = Object.read(q.get('settings'))
        return SendPhoneNumberVerificationCode(phone_number, settings)
