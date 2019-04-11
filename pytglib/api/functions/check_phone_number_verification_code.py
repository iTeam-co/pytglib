

from ..utils import Object


class CheckPhoneNumberVerificationCode(Object):
    """
    Checks the phone number verification code for Telegram Passport 

    Attributes:
        ID (:obj:`str`): ``CheckPhoneNumberVerificationCode``

    Args:
        code (:obj:`str`):
            Verification code

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkPhoneNumberVerificationCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckPhoneNumberVerificationCode":
        code = q.get('code')
        return CheckPhoneNumberVerificationCode(code)
