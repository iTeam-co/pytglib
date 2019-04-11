

from ..utils import Object


class GetActiveLiveLocationMessages(Object):
    """
    Returns all active live locations that should be updated by the client. The list is persistent across application restarts only if the message database is used

    Attributes:
        ID (:obj:`str`): ``GetActiveLiveLocationMessages``

    No parameters required.

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "getActiveLiveLocationMessages"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetActiveLiveLocationMessages":
        
        return GetActiveLiveLocationMessages()
