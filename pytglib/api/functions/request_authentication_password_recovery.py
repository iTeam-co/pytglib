

from ..utils import Object


class RequestAuthenticationPasswordRecovery(Object):
    """
    Requests to send a password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword

    Attributes:
        ID (:obj:`str`): ``RequestAuthenticationPasswordRecovery``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "requestAuthenticationPasswordRecovery"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "RequestAuthenticationPasswordRecovery":
        
        return RequestAuthenticationPasswordRecovery()
