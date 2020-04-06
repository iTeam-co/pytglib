

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
    def read(q: dict, *args) -> "AuthorizationStateWaitTdlibParameters or AuthorizationStateWaitPassword or AuthorizationStateWaitPhoneNumber or AuthorizationStateWaitCode or AuthorizationStateClosed or AuthorizationStateLoggingOut or AuthorizationStateWaitRegistration or AuthorizationStateWaitEncryptionKey or AuthorizationStateReady or AuthorizationStateClosing or AuthorizationStateWaitOtherDeviceConfirmation":
        if q.get("@type"):
            return Object.read(q)
        return AuthorizationState()
