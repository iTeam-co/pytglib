

from ..utils import Object


class UpdateUsersNearby(Object):
    """
    List of users nearby has changed. The update is sent only 60 seconds after a successful searchChatsNearby request 

    Attributes:
        ID (:obj:`str`): ``UpdateUsersNearby``

    Args:
        users_nearby (List of :class:`telegram.api.types.chatNearby`):
            The new list of users nearby

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUsersNearby"

    def __init__(self, users_nearby, **kwargs):
        
        self.users_nearby = users_nearby  # list of chatNearby

    @staticmethod
    def read(q: dict, *args) -> "UpdateUsersNearby":
        users_nearby = [Object.read(i) for i in q.get('users_nearby', [])]
        return UpdateUsersNearby(users_nearby)
