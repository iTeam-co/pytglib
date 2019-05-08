

from ..utils import Object


class SetPassword(Object):
    """
    Changes the password for the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

    Attributes:
        ID (:obj:`str`): ``SetPassword``

    Args:
        old_password (:obj:`str`):
            Previous password of the user 
        new_password (:obj:`str`):
            New password of the user; may be empty to remove the password 
        new_hint (:obj:`str`):
            New password hint; may be empty 
        set_recovery_email_address (:obj:`bool`):
            Pass true if the recovery email address should be changed 
        new_recovery_email_address (:obj:`str`):
            New recovery email address; may be empty

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPassword"

    def __init__(self, old_password, new_password, new_hint, set_recovery_email_address, new_recovery_email_address, extra=None, **kwargs):
        self.extra = extra
        self.old_password = old_password  # str
        self.new_password = new_password  # str
        self.new_hint = new_hint  # str
        self.set_recovery_email_address = set_recovery_email_address  # bool
        self.new_recovery_email_address = new_recovery_email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "SetPassword":
        old_password = q.get('old_password')
        new_password = q.get('new_password')
        new_hint = q.get('new_hint')
        set_recovery_email_address = q.get('set_recovery_email_address')
        new_recovery_email_address = q.get('new_recovery_email_address')
        return SetPassword(old_password, new_password, new_hint, set_recovery_email_address, new_recovery_email_address)
