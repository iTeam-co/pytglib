

from ..utils import Object


class ResendRecoveryEmailAddressCode(Object):
    """
    Resends the 2-step verification recovery email address verification code

    Attributes:
        ID (:obj:`str`): ``ResendRecoveryEmailAddressCode``

    No parameters required.

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendRecoveryEmailAddressCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendRecoveryEmailAddressCode":
        
        return ResendRecoveryEmailAddressCode()
