

from ..utils import Object


class ResendEmailAddressVerificationCode(Object):
    """
    Re-sends the code to verify an email address to be added to a user's Telegram Passport

    Attributes:
        ID (:obj:`str`): ``ResendEmailAddressVerificationCode``

    No parameters required.

    Returns:
        EmailAddressAuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendEmailAddressVerificationCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendEmailAddressVerificationCode":
        
        return ResendEmailAddressVerificationCode()
