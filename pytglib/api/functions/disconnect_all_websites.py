

from ..utils import Object


class DisconnectAllWebsites(Object):
    """
    Disconnects all websites from the current user's Telegram account

    Attributes:
        ID (:obj:`str`): ``DisconnectAllWebsites``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "disconnectAllWebsites"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "DisconnectAllWebsites":
        
        return DisconnectAllWebsites()
