

from ..utils import Object


class AuthorizationStateClosing(Object):
    """
    TDLib is closing, all subsequent queries will be answered with the error 500. Note that closing TDLib can take a while. All resources will be freed only after authorizationStateClosed has been received

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateClosing``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateClosing"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateClosing":
        
        return AuthorizationStateClosing()
