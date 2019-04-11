

from ..utils import Object


class AuthorizationStateWaitTdlibParameters(Object):
    """
    TDLib needs TdlibParameters for initialization

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitTdlibParameters``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitTdlibParameters"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitTdlibParameters":
        
        return AuthorizationStateWaitTdlibParameters()
