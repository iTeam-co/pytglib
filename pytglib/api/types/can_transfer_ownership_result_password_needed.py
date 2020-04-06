

from ..utils import Object


class CanTransferOwnershipResultPasswordNeeded(Object):
    """
    The 2-step verification needs to be enabled first

    Attributes:
        ID (:obj:`str`): ``CanTransferOwnershipResultPasswordNeeded``

    No parameters required.

    Returns:
        CanTransferOwnershipResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "canTransferOwnershipResultPasswordNeeded"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnershipResultPasswordNeeded":
        
        return CanTransferOwnershipResultPasswordNeeded()
