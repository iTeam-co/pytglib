

from ..utils import Object


class SendPhoneNumberConfirmationCode(Object):
    """
    Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation 

    Attributes:
        ID (:obj:`str`): ``SendPhoneNumberConfirmationCode``

    Args:
        hash (:obj:`str`):
            Hash value from the link 
        phone_number (:obj:`str`):
            Phone number value from the link 
        settings (:class:`telegram.api.types.phoneNumberAuthenticationSettings`):
            Settings for the authentication of the user's phone number; pass null to use default settings

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
