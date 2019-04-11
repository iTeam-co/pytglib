

from ..utils import Object


class RecoveryEmailAddress(Object):
    """
    Contains information about the current recovery email address 

    Attributes:
        ID (:obj:`str`): ``RecoveryEmailAddress``

    Args:
        recovery_email_address (:obj:`str`):
            Recovery email address

    Returns:
        RecoveryEmailAddress

    Raises:
        :class:`telegram.Error`
    """
    ID = "recoveryEmailAddress"

    def __init__(self, recovery_email_address, **kwargs):
        
        self.recovery_email_address = recovery_email_address  # str

    @staticmethod
    def read(q: dict, *args) -> "RecoveryEmailAddress":
        recovery_email_address = q.get('recovery_email_address')
        return RecoveryEmailAddress(recovery_email_address)
