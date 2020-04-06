

from ..utils import Object


class CanTransferOwnershipResultOk(Object):
    """
    The session can be used

    Attributes:
        ID (:obj:`str`): ``CanTransferOwnershipResultOk``

    No parameters required.

    Returns:
        CanTransferOwnershipResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "canTransferOwnershipResultOk"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnershipResultOk":
        
        return CanTransferOwnershipResultOk()
