

from ..utils import Object


class Users(Object):
    """
    Represents a list of users 

    Attributes:
        ID (:obj:`str`): ``Users``

    Args:
        total_count (:obj:`int`):
            Approximate total count of users found 
        user_ids (List of :obj:`int`):
            A list of user identifiers

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "users"

    def __init__(self, total_count, user_ids, **kwargs):
        
        self.total_count = total_count  # int
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "Users":
        total_count = q.get('total_count')
        user_ids = q.get('user_ids')
        return Users(total_count, user_ids)
