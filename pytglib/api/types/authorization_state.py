

from ..utils import Object


class AuthorizationState(Object):
    """
    Represents the current authorization state of the TDLib client

    No parameters required.
    """
    ID = "authorizationState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitEncryptionKey or AuthorizationStateReady or AuthorizationStateClosing or AuthorizationStateWaitTdlibParameters or AuthorizationStateLoggingOut or AuthorizationStateWaitCode or AuthorizationStateWaitRegistration or AuthorizationStateWaitPassword or AuthorizationStateWaitOtherDeviceConfirmation or AuthorizationStateClosed or AuthorizationStateWaitPhoneNumber":
        if q.get("@type"):
            return Object.read(q)
        return AuthorizationState()
