

from ..utils import Object


class UpdateAuthorizationState(Object):
    """
    The user authorization state has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateAuthorizationState``

    Args:
        authorization_state (:class:`telegram.api.types.AuthorizationState`):
            New authorization state

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateAuthorizationState"

    def __init__(self, authorization_state, **kwargs):
        
        self.authorization_state = authorization_state  # AuthorizationState

    @staticmethod
    def read(q: dict, *args) -> "UpdateAuthorizationState":
        authorization_state = Object.read(q.get('authorization_state'))
        return UpdateAuthorizationState(authorization_state)
