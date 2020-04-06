

from ..utils import Object


class CanTransferOwnershipResult(Object):
    """
    Represents result of checking whether the current session can be used to transfer a chat ownership to another user

    No parameters required.
    """
    ID = "canTransferOwnershipResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CanTransferOwnershipResultPasswordNeeded or CanTransferOwnershipResultPasswordTooFresh or CanTransferOwnershipResultOk or CanTransferOwnershipResultSessionTooFresh":
        if q.get("@type"):
            return Object.read(q)
        return CanTransferOwnershipResult()
