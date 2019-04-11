

from ..utils import Object


class ConnectedWebsites(Object):
    """
    Contains a list of websites the current user is logged in with Telegram 

    Attributes:
        ID (:obj:`str`): ``ConnectedWebsites``

    Args:
        websites (List of :class:`telegram.api.types.connectedWebsite`):
            List of connected websites

    Returns:
        ConnectedWebsites

    Raises:
        :class:`telegram.Error`
    """
    ID = "connectedWebsites"

    def __init__(self, websites, **kwargs):
        
        self.websites = websites  # list of connectedWebsite

    @staticmethod
    def read(q: dict, *args) -> "ConnectedWebsites":
        websites = [Object.read(i) for i in q.get('websites', [])]
        return ConnectedWebsites(websites)
