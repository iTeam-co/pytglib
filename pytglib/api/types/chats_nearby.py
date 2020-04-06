

from ..utils import Object


class ChatsNearby(Object):
    """
    Represents a list of chats located nearby 

    Attributes:
        ID (:obj:`str`): ``ChatsNearby``

    Args:
        users_nearby (List of :class:`telegram.api.types.chatNearby`):
            List of users nearby 
        supergroups_nearby (List of :class:`telegram.api.types.chatNearby`):
            List of location-based supergroups nearby

    Returns:
        ChatsNearby

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatsNearby"

    def __init__(self, users_nearby, supergroups_nearby, **kwargs):
        
        self.users_nearby = users_nearby  # list of chatNearby
        self.supergroups_nearby = supergroups_nearby  # list of chatNearby

    @staticmethod
    def read(q: dict, *args) -> "ChatsNearby":
        users_nearby = [Object.read(i) for i in q.get('users_nearby', [])]
        supergroups_nearby = [Object.read(i) for i in q.get('supergroups_nearby', [])]
        return ChatsNearby(users_nearby, supergroups_nearby)
