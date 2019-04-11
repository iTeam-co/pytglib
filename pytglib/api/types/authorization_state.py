

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
    def read(q: dict, *args) -> "AuthorizationStateWaitPassword or AuthorizationStateClosing or AuthorizationStateClosed or AuthorizationStateWaitCode or AuthorizationStateWaitPhoneNumber or AuthorizationStateWaitEncryptionKey or AuthorizationStateReady or AuthorizationStateWaitTdlibParameters or AuthorizationStateLoggingOut":
        if q.get("@type"):
            return Object.read(q)
        return AuthorizationState()
