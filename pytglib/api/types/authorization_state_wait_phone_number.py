

from ..utils import Object


class AuthorizationStateWaitPhoneNumber(Object):
    """
    TDLib needs the user's phone number to authorize. Call `setAuthenticationPhoneNumber` to provide the phone number, or use `requestQrCodeAuthentication`, or `checkAuthenticationBotToken` for other authentication options

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
