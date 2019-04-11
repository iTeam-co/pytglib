

from ..utils import Object


class Location(Object):
    """
    Describes a location on planet Earth 

    Attributes:
        ID (:obj:`str`): ``Location``

    Args:
        latitude (:obj:`float`):
            Latitude of the location in degrees; as defined by the sender 
        longitude (:obj:`float`):
            Longitude of the location, in degrees; as defined by the sender

    Returns:
        Location

    Raises:
        :class:`telegram.Error`
    """
    ID = "location"

    def __init__(self, latitude, longitude, **kwargs):
        
        self.latitude = latitude  # float
        self.longitude = longitude  # float

    @staticmethod
    def read(q: dict, *args) -> "Location":
        latitude = q.get('latitude')
        longitude = q.get('longitude')
        return Location(latitude, longitude)
