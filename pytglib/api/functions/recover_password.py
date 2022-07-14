

from ..utils import Object


class RecoverPassword(Object):
    """
    Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up

    Attributes:
        ID (:obj:`str`): ``RecoverPassword``

    Args:
        recovery_code (:obj:`str`):
            Recovery code to check 
        new_password (:obj:`str`):
            New password of the user; may be empty to remove the password 
        new_hint (:obj:`str`):
            New password hint; may be empty

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "recoverPassword"

    def __init__(self, recovery_code, new_password, new_hint, extra=None, **kwargs):
        self.extra = extra
        self.recovery_code = recovery_code  # str
        self.new_password = new_password  # str
        self.new_hint = new_hint  # str

    @staticmethod
    def read(q: dict, *args) -> "RecoverPassword":
        recovery_code = q.get('recovery_code')
        new_password = q.get('new_password')
        new_hint = q.get('new_hint')
        return RecoverPassword(recovery_code, new_password, new_hint)
