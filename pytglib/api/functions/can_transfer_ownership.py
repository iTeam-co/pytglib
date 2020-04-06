

from ..utils import Object


class CanTransferOwnership(Object):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user

    Attributes:
        ID (:obj:`str`): ``CanTransferOwnership``

    No parameters required.

    Returns:
        CanTransferOwnershipResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "canTransferOwnership"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnership":
        
        return CanTransferOwnership()
