

from ..utils import Object


class ResetPassword(Object):
    """
    Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time

    Attributes:
        ID (:obj:`str`): ``ResetPassword``

    No parameters required.

    Returns:
        ResetPasswordResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetPassword"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetPassword":
        
        return ResetPassword()
