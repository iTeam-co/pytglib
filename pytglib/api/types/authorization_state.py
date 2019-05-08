

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
    def read(q: dict, *args) -> "AuthorizationStateReady or AuthorizationStateWaitTdlibParameters or AuthorizationStateWaitPhoneNumber or AuthorizationStateClosing or AuthorizationStateClosed or AuthorizationStateWaitPassword or AuthorizationStateWaitEncryptionKey or AuthorizationStateWaitCode or AuthorizationStateLoggingOut":
        if q.get("@type"):
            return Object.read(q)
        return AuthorizationState()
