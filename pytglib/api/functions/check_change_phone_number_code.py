

from ..utils import Object


class CheckChangePhoneNumberCode(Object):
    """
    Checks the authentication code sent to confirm a new phone number of the user 

    Attributes:
        ID (:obj:`str`): ``CheckChangePhoneNumberCode``

    Args:
        code (:obj:`str`):
            Verification code received by SMS, phone call or flash call

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChangePhoneNumberCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckChangePhoneNumberCode":
        code = q.get('code')
        return CheckChangePhoneNumberCode(code)
