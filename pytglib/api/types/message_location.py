

from ..utils import Object


class MessageLocation(Object):
    """
    A message with a location 

    Attributes:
        ID (:obj:`str`): ``MessageLocation``

    Args:
        location (:class:`telegram.api.types.location`):
            The location description 
        live_period (:obj:`int`):
            Time relative to the message send date, for which the location can be updated, in seconds
        expires_in (:obj:`int`):
            Left time for which the location can be updated, in secondsupdateMessageContent is not sent when this field changes
        heading (:obj:`int`):
            For live locations, a direction in which the location moves, in degrees; 1-360If 0 the direction is unknown
        proximity_alert_radius (:obj:`int`):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000)0 if the notification is disabledAvailable only for the message sender

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageLocation"

    def __init__(self, location, live_period, expires_in, heading, proximity_alert_radius, **kwargs):
        
        self.location = location  # Location
        self.live_period = live_period  # int
        self.expires_in = expires_in  # int
        self.heading = heading  # int
        self.proximity_alert_radius = proximity_alert_radius  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageLocation":
        location = Object.read(q.get('location'))
        live_period = q.get('live_period')
        expires_in = q.get('expires_in')
        heading = q.get('heading')
        proximity_alert_radius = q.get('proximity_alert_radius')
        return MessageLocation(location, live_period, expires_in, heading, proximity_alert_radius)
