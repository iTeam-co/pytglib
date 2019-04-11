

from ..utils import Object


class UpdateUserStatus(Object):
    """
    The user went online or offline 

    Attributes:
        ID (:obj:`str`): ``UpdateUserStatus``

    Args:
        user_id (:obj:`int`):
            User identifier 
        status (:class:`telegram.api.types.UserStatus`):
            New status of the user

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUserStatus"

    def __init__(self, user_id, status, **kwargs):
        
        self.user_id = user_id  # int
        self.status = status  # UserStatus

    @staticmethod
    def read(q: dict, *args) -> "UpdateUserStatus":
        user_id = q.get('user_id')
        status = Object.read(q.get('status'))
        return UpdateUserStatus(user_id, status)
