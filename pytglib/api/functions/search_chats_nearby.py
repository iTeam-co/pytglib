

from ..utils import Object


class SearchChatsNearby(Object):
    """
    Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request should be sent again every 25 seconds with adjusted location to not miss new chats 

    Attributes:
        ID (:obj:`str`): ``SearchChatsNearby``

    Args:
        location (:class:`telegram.api.types.location`):
            Current user location

    Returns:
        ChatsNearby

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchChatsNearby"

    def __init__(self, location, extra=None, **kwargs):
        self.extra = extra
        self.location = location  # Location

    @staticmethod
    def read(q: dict, *args) -> "SearchChatsNearby":
        location = Object.read(q.get('location'))
        return SearchChatsNearby(location)
