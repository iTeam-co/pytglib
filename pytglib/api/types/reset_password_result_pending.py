

from ..utils import Object


class ResetPasswordResultPending(Object):
    """
    The password reset request is pending 

    Attributes:
        ID (:obj:`str`): ``ResetPasswordResultPending``

    Args:
        pending_reset_date (:obj:`int`):
            Point in time (Unix timestamp) after which the password can be reset immediately using resetPassword

    Returns:
        ResetPasswordResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetPasswordResultPending"

    def __init__(self, pending_reset_date, **kwargs):
        
        self.pending_reset_date = pending_reset_date  # int

    @staticmethod
    def read(q: dict, *args) -> "ResetPasswordResultPending":
        pending_reset_date = q.get('pending_reset_date')
        return ResetPasswordResultPending(pending_reset_date)
