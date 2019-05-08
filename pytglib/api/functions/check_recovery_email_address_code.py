

from ..utils import Object


class CheckRecoveryEmailAddressCode(Object):
    """
    Checks the 2-step verification recovery email address verification code 

    Attributes:
        ID (:obj:`str`): ``CheckRecoveryEmailAddressCode``

    Args:
        code (:obj:`str`):
            Verification code

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkRecoveryEmailAddressCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckRecoveryEmailAddressCode":
        code = q.get('code')
        return CheckRecoveryEmailAddressCode(code)
