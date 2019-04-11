

from ..utils import Object


class GetPasswordState(Object):
    """
    Returns the current state of 2-step verification

    Attributes:
        ID (:obj:`str`): ``GetPasswordState``

    No parameters required.

    Returns:
        PasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPasswordState"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetPasswordState":
        
        return GetPasswordState()
