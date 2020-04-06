

from ..utils import Object


class ChatLocation(Object):
    """
    Represents a location to which a chat is connected 

    Attributes:
        ID (:obj:`str`): ``ChatLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            The location 
        address (:obj:`str`):
            Location address; 1-64 characters, as defined by the chat owner

    Returns:
        ChatLocation

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatLocation"

    def __init__(self, location, address, **kwargs):
        
        self.location = location  # Location
        self.address = address  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatLocation":
        location = Object.read(q.get('location'))
        address = q.get('address')
        return ChatLocation(location, address)
