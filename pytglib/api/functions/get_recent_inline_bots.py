

from ..utils import Object


class GetRecentInlineBots(Object):
    """
    Returns up to 20 recently used inline bots in the order of their last usage

    Attributes:
        ID (:obj:`str`): ``GetRecentInlineBots``

    No parameters required.

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecentInlineBots"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetRecentInlineBots":
        
        return GetRecentInlineBots()
