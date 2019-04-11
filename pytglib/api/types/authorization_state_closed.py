

from ..utils import Object


class AuthorizationStateClosed(Object):
    """
    TDLib client is in its final state. All databases are closed and all resources are released. No other updates will be received after this. All queries will be responded towith error code 500. To continue working, one should create a new instance of the TDLib client

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateClosed``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateClosed"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateClosed":
        
        return AuthorizationStateClosed()
