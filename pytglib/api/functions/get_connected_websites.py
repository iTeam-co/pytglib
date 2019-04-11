

from ..utils import Object


class GetConnectedWebsites(Object):
    """
    Returns all website where the current user used Telegram to log in

    Attributes:
        ID (:obj:`str`): ``GetConnectedWebsites``

    No parameters required.

    Returns:
        ConnectedWebsites

    Raises:
        :class:`telegram.Error`
    """
    ID = "getConnectedWebsites"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetConnectedWebsites":
        
        return GetConnectedWebsites()
