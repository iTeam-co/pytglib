

from ..utils import Object


class ResetPasswordResult(Object):
    """
    Represents result of 2-step verification password reset

    No parameters required.
    """
    ID = "resetPasswordResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetPasswordResultOk or ResetPasswordResultDeclined or ResetPasswordResultPending":
        if q.get("@type"):
            return Object.read(q)
        return ResetPasswordResult()
