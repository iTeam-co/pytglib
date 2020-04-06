

from ..utils import Object


class SharePhoneNumber(Object):
    """
    Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber 

    Attributes:
        ID (:obj:`str`): ``SharePhoneNumber``

    Args:
        user_id (:obj:`int`):
            Identifier of the user with whom to share the phone numberThe user must be a mutual contact

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sharePhoneNumber"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SharePhoneNumber":
        user_id = q.get('user_id')
        return SharePhoneNumber(user_id)
