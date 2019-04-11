

from ..utils import Object


class RecoverPassword(Object):
    """
    Recovers the password using a recovery code sent to an email address that was previously set up 

    Attributes:
        ID (:obj:`str`): ``RecoverPassword``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "recoverPassword"

    def __init__(self, recovery_code, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str

    @staticmethod
    def read(q: dict, *args) -> "RecoverPassword":
        recovery_code = q.get('recovery_code')
        return RecoverPassword(recovery_code)
