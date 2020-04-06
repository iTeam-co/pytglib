

from ..utils import Object


class CanTransferOwnershipResultPasswordTooFresh(Object):
    """
    The 2-step verification was enabled recently, user needs to wait 

    Attributes:
        ID (:obj:`str`): ``CanTransferOwnershipResultPasswordTooFresh``

    Args:
        retry_after (:obj:`int`):
            Time left before the session can be used to transfer ownership of a chat, in seconds

    Returns:
        CanTransferOwnershipResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "canTransferOwnershipResultPasswordTooFresh"

    def __init__(self, retry_after, **kwargs):
        
        self.retry_after = retry_after  # int

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnershipResultPasswordTooFresh":
        retry_after = q.get('retry_after')
        return CanTransferOwnershipResultPasswordTooFresh(retry_after)
