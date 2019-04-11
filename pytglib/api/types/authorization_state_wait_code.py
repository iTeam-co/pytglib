

from ..utils import Object


class AuthorizationStateWaitCode(Object):
    """
    TDLib needs the user's authentication code to finalize authorization 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitCode``

    Args:
        is_registered (:obj:`bool`):
            True, if the user is already registered 
        terms_of_service (:class:`telegram.api.types.termsOfService`):
            Telegram terms of service, which should be accepted before user can continue registration; may be null 
        code_info (:class:`telegram.api.types.authenticationCodeInfo`):
            Information about the authorization code that was sent

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitCode"

    def __init__(self, is_registered, terms_of_service, code_info, **kwargs):
        
        self.is_registered = is_registered  # bool
        self.terms_of_service = terms_of_service  # TermsOfService
        self.code_info = code_info  # AuthenticationCodeInfo

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitCode":
        is_registered = q.get('is_registered')
        terms_of_service = Object.read(q.get('terms_of_service'))
        code_info = Object.read(q.get('code_info'))
        return AuthorizationStateWaitCode(is_registered, terms_of_service, code_info)
