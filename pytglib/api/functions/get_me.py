

from ..utils import Object


class GetMe(Object):
    """
    Returns the current user

    Attributes:
        ID (:obj:`str`): ``GetMe``

    No parameters required.

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMe"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetMe":
        
        return GetMe()
