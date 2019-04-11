

from ..utils import Object


class AuthorizationStateReady(Object):
    """
    The user has been successfully authorized. TDLib is now ready to answer queries

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateReady``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateReady"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateReady":
        
        return AuthorizationStateReady()
