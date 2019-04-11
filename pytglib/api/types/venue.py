

from ..utils import Object


class Venue(Object):
    """
    Describes a venue 

    Attributes:
        ID (:obj:`str`): ``Venue``

    Args:
        location (:class:`telegram.api.types.location`):
            Venue location; as defined by the sender 
        title (:obj:`str`):
            Venue name; as defined by the sender 
        address (:obj:`str`):
            Venue address; as defined by the sender 
        provider (:obj:`str`):
            Provider of the venue database; as defined by the senderCurrently only "foursquare" needs to be supported
        id (:obj:`str`):
            Identifier of the venue in the provider database; as defined by the sender 
        type (:obj:`str`):
            Type of the venue in the provider database; as defined by the sender

    Returns:
        Venue

    Raises:
        :class:`telegram.Error`
    """
    ID = "venue"

    def __init__(self, location, title, address, provider, id, type, **kwargs):
        
        self.location = location  # Location
        self.title = title  # str
        self.address = address  # str
        self.provider = provider  # str
        self.id = id  # str
        self.type = type  # str

    @staticmethod
    def read(q: dict, *args) -> "Venue":
        location = Object.read(q.get('location'))
        title = q.get('title')
        address = q.get('address')
        provider = q.get('provider')
        id = q.get('id')
        type = q.get('type')
        return Venue(location, title, address, provider, id, type)
