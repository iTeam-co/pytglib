

from ..utils import Object


class ResetPasswordResultOk(Object):
    """
    The password was reset

    Attributes:
        ID (:obj:`str`): ``ResetPasswordResultOk``

    No parameters required.

    Returns:
        ResetPasswordResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetPasswordResultOk"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetPasswordResultOk":
        
        return ResetPasswordResultOk()
