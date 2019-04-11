

from ..utils import Object


class LinkStateNone(Object):
    """
    The phone number of user A is not known to user B

    Attributes:
        ID (:obj:`str`): ``LinkStateNone``

    No parameters required.

    Returns:
        LinkState

    Raises:
        :class:`telegram.Error`
    """
    ID = "linkStateNone"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LinkStateNone":
        
        return LinkStateNone()
