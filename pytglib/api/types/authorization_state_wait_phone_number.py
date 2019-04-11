

from ..utils import Object


class AuthorizationStateWaitPhoneNumber(Object):
    """
    TDLib needs the user's phone number to authorize

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitPhoneNumber``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitPhoneNumber":
        
        return AuthorizationStateWaitPhoneNumber()
