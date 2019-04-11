

from ..utils import Object


class UpdateUserFullInfo(Object):
    """
    Some data from userFullInfo has been changed 

    Attributes:
        ID (:obj:`str`): ``UpdateUserFullInfo``

    Args:
        user_id (:obj:`int`):
            User identifier 
        user_full_info (:class:`telegram.api.types.userFullInfo`):
            New full information about the user

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUserFullInfo"

    def __init__(self, user_id, user_full_info, **kwargs):
        
        self.user_id = user_id  # int
        self.user_full_info = user_full_info  # UserFullInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateUserFullInfo":
        user_id = q.get('user_id')
        user_full_info = Object.read(q.get('user_full_info'))
        return UpdateUserFullInfo(user_id, user_full_info)
