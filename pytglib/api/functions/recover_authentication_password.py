

from ..utils import Object


class RecoverAuthenticationPassword(Object):
    """
    Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword 

    Attributes:
        ID (:obj:`str`): ``RecoverAuthenticationPassword``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "recoverAuthenticationPassword"

    def __init__(self, recovery_code, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str

    @staticmethod
    def read(q: dict, *args) -> "RecoverAuthenticationPassword":
        recovery_code = q.get('recovery_code')
        return RecoverAuthenticationPassword(recovery_code)
