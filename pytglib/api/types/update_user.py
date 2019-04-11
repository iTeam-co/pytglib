

from ..utils import Object


class UpdateUser(Object):
    """
    Some data of a user has changed. This update is guaranteed to come before the user identifier is returned to the client 

    Attributes:
        ID (:obj:`str`): ``UpdateUser``

    Args:
        user (:class:`telegram.api.types.user`):
            New data about the user

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUser"

    def __init__(self, user, **kwargs):
        
        self.user = user  # User

    @staticmethod
    def read(q: dict, *args) -> "UpdateUser":
        user = Object.read(q.get('user'))
        return UpdateUser(user)
