

from ..utils import Object


class GetCurrentState(Object):
    """
    Returns all updates needed to restore current TDLib state, i.e. all actual UpdateAuthorizationState/UpdateUser/UpdateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization

    Attributes:
        ID (:obj:`str`): ``GetCurrentState``

    No parameters required.

    Returns:
        Updates

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCurrentState"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetCurrentState":
        
        return GetCurrentState()
