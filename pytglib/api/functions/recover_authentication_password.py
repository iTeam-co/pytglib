

from ..utils import Object


class RecoverAuthenticationPassword(Object):
    """
    Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword

    Attributes:
        ID (:obj:`str`): ``RecoverAuthenticationPassword``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check 
        new_password (:obj:`str`):
            New password of the user; may be empty to remove the password 
        new_hint (:obj:`str`):
            New password hint; may be empty

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "recoverAuthenticationPassword"

    def __init__(self, recovery_code, new_password, new_hint, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str
        self.new_password = new_password  # str
        self.new_hint = new_hint  # str

    @staticmethod
    def read(q: dict, *args) -> "RecoverAuthenticationPassword":
        recovery_code = q.get('recovery_code')
        new_password = q.get('new_password')
        new_hint = q.get('new_hint')
        return RecoverAuthenticationPassword(recovery_code, new_password, new_hint)
