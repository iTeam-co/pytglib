

from ..utils import Object


class ResetPasswordResultDeclined(Object):
    """
    The password reset request was declined 

    Attributes:
        ID (:obj:`str`): ``ResetPasswordResultDeclined``

    Args:
        retry_date (:obj:`int`):
            Point in time (Unix timestamp) when the password reset can be retried

    Returns:
        ResetPasswordResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetPasswordResultDeclined"

    def __init__(self, retry_date, **kwargs):
        
        self.retry_date = retry_date  # int

    @staticmethod
    def read(q: dict, *args) -> "ResetPasswordResultDeclined":
        retry_date = q.get('retry_date')
        return ResetPasswordResultDeclined(retry_date)
