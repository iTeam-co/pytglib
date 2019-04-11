

from ..utils import Object


class CheckEmailAddressVerificationCode(Object):
    """
    Checks the email address verification code for Telegram Passport 

    Attributes:
        ID (:obj:`str`): ``CheckEmailAddressVerificationCode``

    Args:
        code (:obj:`str`):
            Verification code

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkEmailAddressVerificationCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckEmailAddressVerificationCode":
        code = q.get('code')
        return CheckEmailAddressVerificationCode(code)
