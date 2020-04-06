

from ..utils import Object


class AuthorizationStateWaitRegistration(Object):
    """
    The user is unregistered and need to accept terms of service and enter their first name and last name to finish registration 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitRegistration``

    Args:
        terms_of_service (:class:`telegram.api.types.termsOfService`):
            Telegram terms of service

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitRegistration"

    def __init__(self, terms_of_service, **kwargs):
        
        self.terms_of_service = terms_of_service  # TermsOfService

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitRegistration":
        terms_of_service = Object.read(q.get('terms_of_service'))
        return AuthorizationStateWaitRegistration(terms_of_service)
