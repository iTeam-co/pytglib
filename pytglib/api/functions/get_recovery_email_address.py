

from ..utils import Object


class GetRecoveryEmailAddress(Object):
    """
    Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user 

    Attributes:
        ID (:obj:`str`): ``GetRecoveryEmailAddress``

    Args:
        password (:obj:`str`):
            The password for the current user

    Returns:
        RecoveryEmailAddress

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecoveryEmailAddress"

    def __init__(self, password, extra=None, **kwargs):
        self.extra = extra
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "GetRecoveryEmailAddress":
        password = q.get('password')
        return GetRecoveryEmailAddress(password)
