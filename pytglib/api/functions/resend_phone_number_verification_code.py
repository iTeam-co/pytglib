

from ..utils import Object


class ResendPhoneNumberVerificationCode(Object):
    """
    Re-sends the code to verify a phone number to be added to a user's Telegram Passport

    Attributes:
        ID (:obj:`str`): ``ResendPhoneNumberVerificationCode``

    No parameters required.

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendPhoneNumberVerificationCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendPhoneNumberVerificationCode":
        
        return ResendPhoneNumberVerificationCode()
