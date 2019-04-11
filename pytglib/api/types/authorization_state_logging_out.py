

from ..utils import Object


class AuthorizationStateLoggingOut(Object):
    """
    The user is currently logging out

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateLoggingOut``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateLoggingOut"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateLoggingOut":
        
        return AuthorizationStateLoggingOut()
