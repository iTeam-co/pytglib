

from ..utils import Object


class SetRecoveryEmailAddress(Object):
    """
    Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed.If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation 

    Attributes:
        ID (:obj:`str`): ``SetRecoveryEmailAddress``

    Args:
        password (:obj:`str`):
            Password of the current user 
        new_recovery_email_address (:obj:`str`):
            New recovery email address

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "setRecoveryEmailAddress"

    def __init__(self, password, new_recovery_email_address, extra=None, **kwargs):
        self.extra = extra
        self.password = password  # str
        self.new_recovery_email_address = new_recovery_email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "SetRecoveryEmailAddress":
        password = q.get('password')
        new_recovery_email_address = q.get('new_recovery_email_address')
        return SetRecoveryEmailAddress(password, new_recovery_email_address)
