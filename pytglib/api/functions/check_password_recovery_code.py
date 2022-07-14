

from ..utils import Object


class CheckPasswordRecoveryCode(Object):
    """
    Checks whether a 2-step verification password recovery code sent to an email address is valid 

    Attributes:
        ID (:obj:`str`): ``CheckPasswordRecoveryCode``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkPasswordRecoveryCode"

    def __init__(self, recovery_code, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckPasswordRecoveryCode":
        recovery_code = q.get('recovery_code')
        return CheckPasswordRecoveryCode(recovery_code)
