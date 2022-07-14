

from ..utils import Object


class InputMessageLocation(Object):
    """
    A message with a location 

    Attributes:
        ID (:obj:`str`): ``InputMessageLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            Location to be sent 
        live_period (:obj:`int`):
            Period for which the location can be updated, in seconds; must be between 60 and 86400 for a live location and 0 otherwise
        heading (:obj:`int`):
            For live locations, a direction in which the location moves, in degrees; 1-360Pass 0 if unknown
        proximity_alert_radius (:obj:`int`):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000)Pass 0 if the notification is disabledCan't be enabled in channels and Saved Messages

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageLocation"

    def __init__(self, location, live_period, heading, proximity_alert_radius, **kwargs):
        
        self.location = location  # Location
        self.live_period = live_period  # int
        self.heading = heading  # int
        self.proximity_alert_radius = proximity_alert_radius  # int

    @staticmethod
    def read(q: dict, *args) -> "InputMessageLocation":
        location = Object.read(q.get('location'))
        live_period = q.get('live_period')
        heading = q.get('heading')
        proximity_alert_radius = q.get('proximity_alert_radius')
        return InputMessageLocation(location, live_period, heading, proximity_alert_radius)
