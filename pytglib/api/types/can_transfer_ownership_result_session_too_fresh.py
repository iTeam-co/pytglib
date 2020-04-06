

from ..utils import Object


class CanTransferOwnershipResultSessionTooFresh(Object):
    """
    The session was created recently, user needs to wait 

    Attributes:
        ID (:obj:`str`): ``CanTransferOwnershipResultSessionTooFresh``

    Args:
        retry_after (:obj:`int`):
            Time left before the session can be used to transfer ownership of a chat, in seconds

    Returns:
        CanTransferOwnershipResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "canTransferOwnershipResultSessionTooFresh"

    def __init__(self, retry_after, **kwargs):
        
        self.retry_after = retry_after  # int

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnershipResultSessionTooFresh":
        retry_after = q.get('retry_after')
        return CanTransferOwnershipResultSessionTooFresh(retry_after)
