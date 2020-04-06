

from ..utils import Object


class SendPhoneNumberConfirmationCode(Object):
    """
    Sends phone number confirmation code. Should be called when user presses "https://t.me/confirmphone?phone=*******&hash=**********" or "tg://confirmphone?phone=*******&hash=**********" link 

    Attributes:
        ID (:obj:`str`): ``SendPhoneNumberConfirmationCode``

    Args:
        hash (:obj:`str`):
            Value of the "hash" parameter from the link
        phone_number (:obj:`str`):
            Value of the "phone" parameter from the link 
        settings (:class:`telegram.api.types.phoneNumberAuthenticationSettings`):
            Settings for the authentication of the user's phone number

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPhoneNumberConfirmationCode"

    def __init__(self, hash, phone_number, settings, extra=None, **kwargs):
        self.extra = extra
        self.hash = hash  # str
        self.phone_number = phone_number  # str
        self.settings = settings  # PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict, *args) -> "SendPhoneNumberConfirmationCode":
        hash = q.get('hash')
        phone_number = q.get('phone_number')
        settings = Object.read(q.get('settings'))
        return SendPhoneNumberConfirmationCode(hash, phone_number, settings)
