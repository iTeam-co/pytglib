

from ..utils import Object


class GetUserFullInfo(Object):
    """
    Returns full information about a user by their identifier 

    Attributes:
        ID (:obj:`str`): ``GetUserFullInfo``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        UserFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getUserFullInfo"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetUserFullInfo":
        user_id = q.get('user_id')
        return GetUserFullInfo(user_id)
