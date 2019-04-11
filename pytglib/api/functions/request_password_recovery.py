

from ..utils import Object


class RequestPasswordRecovery(Object):
    """
    Requests to send a password recovery code to an email address that was previously set up

    Attributes:
        ID (:obj:`str`): ``RequestPasswordRecovery``

    No parameters required.

    Returns:
        EmailAddressAuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "requestPasswordRecovery"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "RequestPasswordRecovery":
        
        return RequestPasswordRecovery()
