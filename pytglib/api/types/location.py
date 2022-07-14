

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
        horizontal_accuracy (:obj:`float`):
            The estimated horizontal accuracy of the location, in meters; as defined by the sender0 if unknown

    Returns:
        Location

    Raises:
        :class:`telegram.Error`
    """
    ID = "location"

    def __init__(self, latitude, longitude, horizontal_accuracy, **kwargs):
        
        self.latitude = latitude  # float
        self.longitude = longitude  # float
        self.horizontal_accuracy = horizontal_accuracy  # float

    @staticmethod
    def read(q: dict, *args) -> "Location":
        latitude = q.get('latitude')
        longitude = q.get('longitude')
        horizontal_accuracy = q.get('horizontal_accuracy')
        return Location(latitude, longitude, horizontal_accuracy)
