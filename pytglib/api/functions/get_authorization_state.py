

from ..utils import Object


class GetAuthorizationState(Object):
    """
    Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state

    Attributes:
        ID (:obj:`str`): ``GetAuthorizationState``

    No parameters required.

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAuthorizationState"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetAuthorizationState":
        
        return GetAuthorizationState()
