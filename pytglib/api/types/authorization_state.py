

from ..utils import Object


class AuthorizationState(Object):
    """
    Represents the current authorization state of the client

    No parameters required.
    """
    ID = "authorizationState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitCode or AuthorizationStateWaitEncryptionKey or AuthorizationStateReady or AuthorizationStateWaitPhoneNumber or AuthorizationStateWaitPassword or AuthorizationStateLoggingOut or AuthorizationStateClosing or AuthorizationStateClosed or AuthorizationStateWaitTdlibParameters":
        if q.get("@type"):
            return Object.read(q)
        return AuthorizationState()
