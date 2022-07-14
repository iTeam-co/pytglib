

from ..utils import Object


class CheckAuthenticationPasswordRecoveryCode(Object):
    """
    Checks whether a password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword 

    Attributes:
        ID (:obj:`str`): ``CheckAuthenticationPasswordRecoveryCode``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkAuthenticationPasswordRecoveryCode"

    def __init__(self, recovery_code, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckAuthenticationPasswordRecoveryCode":
        recovery_code = q.get('recovery_code')
        return CheckAuthenticationPasswordRecoveryCode(recovery_code)
