

from ..utils import Object


class AuthorizationStateWaitCode(Object):
    """
    TDLib needs the user's authentication code to authorize 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitCode``

    Args:
        code_info (:class:`telegram.api.types.authenticationCodeInfo`):
            Information about the authorization code that was sent

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitCode"

    def __init__(self, code_info, **kwargs):
        
        self.code_info = code_info  # AuthenticationCodeInfo

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitCode":
        code_info = Object.read(q.get('code_info'))
        return AuthorizationStateWaitCode(code_info)
