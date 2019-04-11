

from ..utils import Object


class SendEmailAddressVerificationCode(Object):
    """
    Sends a code to verify an email address to be added to a user's Telegram Passport 

    Attributes:
        ID (:obj:`str`): ``SendEmailAddressVerificationCode``

    Args:
        email_address (:obj:`str`):
            Email address

    Returns:
        EmailAddressAuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendEmailAddressVerificationCode"

    def __init__(self, email_address, extra=None, **kwargs):
        self.extra = extra
        self.email_address = email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "SendEmailAddressVerificationCode":
        email_address = q.get('email_address')
        return SendEmailAddressVerificationCode(email_address)
